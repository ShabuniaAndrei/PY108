import config
import keyboard
import logging
import requests
from aiogram import Bot, types, executor, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from lxml import html

storage = MemoryStorage()
bot = Bot(token=config.token_bot, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'#levelname-8s [%(asctime)s]%(message)s',
                    filename='log.txt', level=logging.INFO)


@dp.message_handler(commands='start')
async def welcome(message):
    await bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}\n'
                                            f'', reply_markup=keyboard.start, parse_mode='Markdown')


@dp.message_handler(content_types=['text'])
async def get_message(message):
    if message.text == 'Информация':
        user_id = message.from_user.id
        await bot.send_message(message.chat.id, text=f'Твой ID: {user_id}')
    elif message.text == 'Погода':
        page = requests.get('https://gismeteo.by', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
        }).text
        pars_weather_page = html.fromstring(page)
        city = pars_weather_page.xpath('//a[@class="city-link link"]//text()')[0]
        time = pars_weather_page.xpath('//div[@class="current-time"]//text()')[0]
        descr = pars_weather_page.xpath('//div[@class="weather-description"]//text()')[0]
        humidity = pars_weather_page.xpath('//div[@class="item-value"]//text()')[14]
        degrees = ''.join(pars_weather_page.xpath('//div[@class="temperature"]//text()')[:2])
        feeling = ''.join(pars_weather_page.xpath('//div[@class="item-value"]//text()')[:2])
        wind = pars_weather_page.xpath('//div[@class="item-value"]//text()')[4]
        await bot.send_message(message.chat.id, text=f'Сегодня: {time}\n{city}, {degrees}\n{descr}\nВетер: {wind} м/с\n'
                                                     f'Влажность: {humidity}%\nПо ощущению: {feeling}')
    elif message.text == 'Cписок полезной литературы для разработчиков Python':
        page = requests.get('https://it-math.ru/spisok-literatury-python/', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
        }).text
        pars_list_page = html.fromstring(page)
        pars_list = pars_list_page.xpath('//div[@class="entry-content cf"]//text()')
        pars_list_redact = map(lambda x: x.replace('\n', '\n\n'), pars_list[2:-4])
        result = " ".join(map(str, pars_list_redact))
        await bot.send_message(message.chat.id, text=f'{result}')


if __name__ == '__main__':
    print('Bot started')
    executor.start_polling(dp, skip_updates=True)
