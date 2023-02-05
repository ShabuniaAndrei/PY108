from aiogram import types
start = types.ReplyKeyboardMarkup(resize_keyboard=True)
info = types.KeyboardButton('Информация')
weather = types.KeyboardButton('Погода')
link = types.KeyboardButton('Cписок полезной литературы для разработчиков Python')
start.add(info, weather)
start.add(link)