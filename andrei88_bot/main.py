# import config
import keyboard
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import time
import logging
import requests
from lxml import html

storage = MemoryStorage()
bot = Bot(token=config.bot_key, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot, storage=storage)

logging.basicConfig(format=u'#levelname-8s [%(asctime)s]'
                           u'%(message)s',
                    filename='log.txt',
                    level=logging.INFO)


# ---------------------start button
@dp.message_handler(commands='start', commands_prefix='!/', state=None)
async def welcome(message):
    joined_file = open('users_data.txt', 'r')
    joined_users = set()
    for line in joined_file:
        joined_users.add(line.strip())
    if not str(message.chat.id) in joined_users:
        joined_file = open('users_data.txt', 'a')
        joined_file.write(str(message.chat.id))
        joined_users.add(message.chat.id)

    await bot.send_message(message.chat.id, f'Привет мышечь "{message.from_user.first_name}"'
                                            f'\nЧе кого сучара?', reply_markup=keyboard.start, parse_mode='Markdown')
#
#
# # ------------information button
# @dp.message_handler(content_types=['text'])
# async def get_message(message):
#     if message.text == 'ЧЕ':
#         await bot.send_message(message.chat.id, text=f'НУ ЧЕ, ПРИВЕТ МЫШАРА')
#
#     elif message.text == 'КОГО':
#         await bot.send_message(message.chat.id, text=f'КОГО-ЧТО, МЫШАРА?')
#
#     elif message.text == 'СУЧАРА':
#         await bot.send_message(message.chat.id, text=f'ЧЕ СУЧАРА, ТЫКАЕШЬ?')
#
#     elif message.text == 'ПОГОДА':
#         page = requests.get('https://gismeteo.by', headers={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
#         }).text
#
#         tree = html.fromstring(page.content)
#         city = tree.xpath('//a[@class="city-link link"]//text()')[0]
#         time = tree.xpath('//div[@class="current-time"]//text()')[0]
#         descr = tree.xpath('//div[@class="weather-description"]//text()')[0]
#         degrees = ''.join(tree.xpath('//div[@class="temperature"]//text()')[:2])
#         await bot.send_message(message.chat.id, text=f'Скоро будет погода..')
#
#
# if __name__ == '__main__':
#     print('Bot started')
#     executor.start_polling(dp, skip_updates=True)
