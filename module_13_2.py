from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

from pyexpat.errors import messages

api = '7961462971:AAHBNMb7_3cy64-jMoy8M6Ku91RSm98jqqM'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот, помогающий твоему здоровьюю.')
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)