from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# keyboard for client
b_start = KeyboardButton('/start')
b_info = KeyboardButton('/info')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b_info)

# keyboard for info message
b_site = InlineKeyboardButton(text='Мой сайт', url='https://damir-ernazarov-yesspeace.carrd.co/')

kb_info = InlineKeyboardMarkup(resize_keyboard=True)

kb_info.insert(b_site)
