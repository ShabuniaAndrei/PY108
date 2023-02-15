from aiogram import types

start = types.ReplyKeyboardMarkup(resize_keyboard=True)

info = types.KeyboardButton('СУЧАРА')
stats = types.KeyboardButton('ЧЕ')

weather = types.KeyboardButton('КОГО')

weathers = types.KeyboardButton('ПОГОДА')

start.add(info, stats)
start.add(weather, weathers)
