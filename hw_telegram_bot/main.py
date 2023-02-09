import asyncio
import logging
import requests
import config
import keyboard
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from lxml import html
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(token=config.token_bot, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'#levelname-8s [%(asctime)s]%(message)s',
                    filename='log.txt', level=logging.INFO)


class Me_info(StatesGroup):
    Q1 = State()
    Q2 = State()


@dp.message_handler(Command('me'), state=None)
async def enter_me_info(message: types.Message):
    if message.chat.id == config.admin:
        await message.answer('Ведется запись...\n'
                             '1) Введите ссылку:',
                             parse_mode='Markdown')
        await Me_info.Q1.set()  # Начинаем ждать ответ от пользователя/админа


@dp.message_handler(state=Me_info.Q1)  # выполнитсчя только тогда, когда будет получем ответ от пользователя
async def answer_for_q1(message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer('Ссылка сохранена\n'
                         '2) Введите описание:')
    await Me_info.Q2.set()


@dp.message_handler(state=Me_info.Q2)  # выполнитсчя только тогда, когда будет получем ответ от пользователя
async def answer_for_q2(message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)

    await message.answer('Ссылка и описание сохранены!')

    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = data.get('answer2')

    with open('link.txt', 'w', encoding='utf-8') as joined_file:
        joined_file.write(str(answer1))

    with open('text.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(str(answer2))

    await message.answer(f"Ваша ссылка: {answer1}, Описание: {answer2}")

    await state.finish()


@dp.message_handler(commands='start', commands_prefix='!/', state=None)
async def welcome(message):
    joined_file = open('users_data.txt', 'r')
    joined_users = set()
    for line in joined_file:
        joined_users.add(line.strip())
    if not str(message.chat.id) in joined_users:
        joined_file = open('users_data.txt', 'a')
        joined_file.write(str(message.chat.id) + '\n')
        joined_users.add(message.chat.id)

    await bot.send_message(message.chat.id, f"Привет *{message.from_user.first_name}*,\nДавно не виделись!",
                           reply_markup=keyboard.start, parse_mode='Markdown')


@dp.callback_query_handler(text_contains='join')
async def join(call):
    if call.message.chat.id == config.admin:
        users = sum(1 for _ in open('users_data.txt'))
        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text=f"Бот использует {users} пользователей",
                                    parse_mode='Markdown')
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text=f"Инфа только для админа",
                                    parse_mode='Markdown')


@dp.callback_query_handler(text_contains='cancel')
async def cancel(call):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=f"Ты вернулся в главное меню",
                                parse_mode='Markdown')


@dp.callback_query_handler(text_contains='user_id')
async def user_id(call):
    id_user = call.from_user.id
    await bot.send_message(chat_id=call.message.chat.id,
                           text=f'Твой ID: {id_user}',
                           parse_mode='Markdown')


@dp.callback_query_handler(text_contains='return_back')
async def return_back(call):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=f"Вы отменили выбор",
                                parse_mode='Markdown')


@dp.message_handler(commands='send')
async def send(message):
    if message.chat.id == config.admin:
        await bot.send_message(message.chat.id, f"Старт рассылки...",
                               parse_mode='Markdown')
        rec_user, block_user = 0, 0
        with open('users_data.txt', 'r') as file:
            joined_users = set()  # создадим множество
            for line in file:  # итерируемся по файлу
                joined_users.add(line.strip())  # каждую строку (в строке id) записываем во множество
            for user in joined_users:
                try:
                    await bot.send_photo(user, open('744483_original.png', 'rb'), message.text[message.text.find(''):])
                    rec_user += 1
                except:
                    block_user += 1
                await asyncio.sleep(0.4)
            await bot.send_message(message.chat.id, f"Рассылка закончена!\n"
                                                    f"Отправлено пользователям: {rec_user}\n"
                                                    f"Заблокировано пользователей: {block_user}",
                                   parse_mode='Markdown')


@dp.message_handler(content_types=['text'])
async def get_message(message):
    if message.text == 'Информация':
        await bot.send_message(message.chat.id, text=f'Хочешь посмотреть статистику?',
                               reply_markup=keyboard.stats,
                               parse_mode='Markdown')
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
    elif message.text == 'Разработчик':
        with open('link.txt', 'r', encoding='UTF-8') as link:
            link = link.read()
        with open('text.txt', 'r', encoding='UTF-8') as text:
            text = text.read()
        await bot.send_message(message.chat.id, f'Заходи на {link}\n{text}', parse_mode='HTML')
    elif message.text == 'Покажи пользователя':
        await bot.send_message(message.chat.id, text=f'Выбери вариант',
                               reply_markup=keyboard.user,
                               parse_mode='Markdown')
    elif message.text == 'Отправить фото':
        await bot.send_photo(message.chat.id, open('744177_original.png', 'rb'),
                             reply_markup=keyboard.send_photo,
                             parse_mode='Markdown')


if __name__ == '__main__':
    print('Bot started')
    executor.start_polling(dp, skip_updates=True)
