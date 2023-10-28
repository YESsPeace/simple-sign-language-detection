from io import BytesIO

import cv2
import numpy as np
import requests
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import dp, bot, model
from functions import recognize_sign_from_img
from bucket import media_without_photo
from keyboards import kb_client, kb_info

# Максимальный допустимый размер фотографии в байтах
MAX_PHOTO_SIZE_BYTES = 5 * 1024 * 1024  # 5 МБ


class FSMClient(StatesGroup):
    solution = State()


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(
        'Привет, я бот, который распознает жесты руки с картинки. Просто вышли мне фотокарточку с жестом руки.',
        reply_markup=kb_client
    )

    await bot.send_video(message.chat.id, video='https://i.imgur.com/ivDfNgl.gif')


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer(
        'Это бот для взаимодействия с нейросетею, которая расспознаёт жесты рук. Бот реагирует только на картинки и распознаёт на них знаки. Просто вышлите ему картинку, и в ответном сообщении бот выдаст картинку с распознанным знаком.',
        reply_markup=kb_client
    )


@dp.message_handler(commands=['info'])
async def command_info(message: types.Message):
    await message.answer(
        'Это бот для взаимодействия с нейросетею, которая расспознаёт жесты рук. ',
        reply_markup=kb_info
    )


@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    try:
        photo = message.photo[3]

        # Получаем изображение как байтовый объект
        file_id = photo.file_id

        file_info = await bot.get_file(file_id)
        file_size = file_info.file_size

        if file_size > MAX_PHOTO_SIZE_BYTES:
            await message.answer("Сорри, но ваше изображение слишком большое. Максимальный объем - 5 МБ.")
            breakpoint()

        image_url = f"https://api.telegram.org/bot{bot._token}/getFile?file_id={file_id}"
        response = requests.get(image_url)
        image_path = response.json()['result']['file_path']
        image_data = BytesIO(requests.get(f"https://api.telegram.org/file/bot{bot._token}/{image_path}").content)

        # Преобразовываем байтовый объект в изображение с помощью OpenCV
        image = cv2.imdecode(np.frombuffer(image_data.read(), np.uint8), cv2.IMREAD_COLOR)

        # Обработка изображения
        image = recognize_sign_from_img(image, model)

        # Преобразование обработанного изображения в байты для отправки
        ret, image_data = cv2.imencode(".jpg", image)
        image_bytes = BytesIO(image_data.tobytes())

        # Отправка обработанного изображения в ответ на сообщение
        await bot.send_photo(message.chat.id, photo=image_bytes)

    except Exception as e:
        print(f"Ошибка: {e}")


@dp.message_handler(content_types=media_without_photo)
async def handle_other_media(message: types.Message):
    await message.answer(
        'Нет-нет-нет, я могу распознать жест только с фото, сорри.',
        reply_markup=kb_client
    )


@dp.message_handler(content_types=['text'])
async def handle_any_text(message: types.Message):
    await message.answer(
        'Сорри, текст не понимаю, только команды.',
        reply_markup=kb_client
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_info, commands=['info'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(handle_photo, content_types=['photo'])
    dp.register_message_handler(handle_other_media, content_types=media_without_photo)
    dp.register_message_handler(handle_any_text, content_types=['text'])
