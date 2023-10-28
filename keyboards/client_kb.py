from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# keyboard for client
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

b_help = KeyboardButton('/help')
b_info = KeyboardButton('/info')

kb_client.add(b_help)
kb_client.add(b_info)

# keyboard for info message
kb_info = InlineKeyboardMarkup(resize_keyboard=True)

b_site = InlineKeyboardButton(text='Мой сайт', url='https://damir-ernazarov-yesspeace.carrd.co/')

kb_info.insert(b_site)
