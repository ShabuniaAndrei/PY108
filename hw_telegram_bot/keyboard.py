from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)

stats = types.KeyboardButton('Информация')
weather = types.KeyboardButton('Погода')
link = types.KeyboardButton('Cписок полезной литературы для разработчиков Python')
developer = types.KeyboardButton('Разработчик')
user = types.KeyboardButton('Покажи пользователя')
send_photo = types.KeyboardButton('Отправить фото')

start.add(stats, weather)
start.add(link)
start.add(developer, user)
start.add(send_photo)
stats = InlineKeyboardMarkup()
stats.add(InlineKeyboardButton(f'YES', callback_data='join'))
stats.add(InlineKeyboardButton(f'NO', callback_data='cancel'))
user = InlineKeyboardMarkup()
user.add(InlineKeyboardButton(f'Хочу увидеть id', callback_data='user_id'))
user.add(InlineKeyboardButton(f'Вернуться обратно', callback_data='return_back'))
