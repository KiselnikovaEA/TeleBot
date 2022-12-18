from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import dotenv_values

config = dotenv_values(".env")

bot = Bot(config['TOKEN'])
dp = Dispatcher(bot)

horo_sign = {
    'Овен': 'https://horo.mail.ru/prediction/aries/today/',
    'Телец': 'https://horo.mail.ru/prediction/taurus/today/',
    'Близнецы': 'https://horo.mail.ru/prediction/gemini/today/',
    'Рак': 'https://horo.mail.ru/prediction/cancer/today/',
    'Лев': 'https://horo.mail.ru/prediction/leo/today/',
    'Дева': 'https://horo.mail.ru/prediction/virgo/today/',
    'Весы': 'https://horo.mail.ru/prediction/libra/today/',
    'Скорпион': 'https://horo.mail.ru/prediction/scorpio/today/',
    'Стрелец': 'https://horo.mail.ru/prediction/sagittarius/today/',
    'Козерог': 'https://horo.mail.ru/prediction/capricorn/today/',
    'Водолей': 'https://horo.mail.ru/prediction/aquarius/today/',
    'Рыбы': 'https://horo.mail.ru/prediction/pisces/today/'
    }

# Клавиатура с обычными кнопками
b1 = KeyboardButton('/Хочу')
b2 = KeyboardButton('/Обойдусь')
kb_answer = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_answer.add(b1).add(b2)

# Инлайн-кнопки
kb_horoscope = InlineKeyboardMarkup(row_width=1)
for sign in horo_sign:
    urlButton = InlineKeyboardButton(text = sign, url=horo_sign[sign])
    kb_horoscope.add(urlButton)

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    welcome_text = 'Приветик! Я - Люся, ученица академии здравого смысла! Но пока я мало, что умею. Хочешь, покажу гороскоп?'
    await bot.send_message(message.from_user.id, welcome_text, reply_markup=kb_answer)


@dp.message_handler(commands=['Хочу'])
async def go_horoscope(message : types.Message): # 
    text = 'Суеверный и странный! Ведь ты обязательно всего добъешься, если приложишь достаточно усилий, встретишься с нужными людьми, если договоришься \
        и придёшь, и разбогатеешь, если заработаешь денег. Тебе не нужен для этого гороскоп. Но, если ты настаиваешь...'
    await bot.send_message(message.from_user.id, text, reply_markup=kb_horoscope)

@dp.message_handler(commands=['Обойдусь'])
async def no_horoscope(message : types.Message):
    text = 'Да, ты моя радость! Я сразу поняла, что ты не веришь в эту чепуху. Заходи через месяцок, я ещё чему-нибудь научусь.'
    await bot.send_message(message.from_user.id, text, reply_markup=ReplyKeyboardRemove())


executor.start_polling(dp, skip_updates=True)