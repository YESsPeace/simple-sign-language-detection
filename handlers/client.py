from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text

from config import dp, bot, model
from keyboards import kb_client, kb_info


class FSMClient(StatesGroup):
    solution = State()


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(
        'Привет, я бот, который распознает жесты руки с картинки или кружочка до. Просто вышли мне фотокарточку или '
        'кружочек с жестом руки.',
        reply_markup=kb_client
    )


@dp.message_handler(commands=['help', 'info'])
async def command_start(message: types.Message):
    await message.answer(
        'Это бот для взаимодействия с нейросетею, которая расспознаёт жесты рук. Данную нейросеть разработал я, '
        'Эрназаров Дамир. Подробнее о мой деятельности на сайте',
        reply_markup=kb_info
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_start, commands=['help', 'info'])
