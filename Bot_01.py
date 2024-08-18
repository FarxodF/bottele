from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

# Замените 'YOUR_API_KEY' на ваш реальный API-ключ
API_KEY = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(messeage: types.Message):
    print('Введите команду /start, что бы начать общение.')


if __name__=='__main__':
    print('Бот запущен и готов к работе.')
    executor.start_polling(dp, skip_updates=True)
