import logging
from aiogram import Bot, Dispatcher, executor, types
import config
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup

TOKEN = "Token"
chat_id = "user"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

but1 = "Курсовая"
but2 = "Диплом"
but3 = "Реферат"

kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(but1, but2, but3)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет", reply_markup=kb1)

@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.answer("Убираем шаблоны сообщений", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(content_types=['document'])
async def send(message: types.Message):
    await message.answer("Принято")
    await bot.send_message(chat_id, message.document)

@dp.message_handler(text='Курсовая')
async def send_welcome(message: types.Message):
    await message.answer("Пришлите Тему", reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id, message.text)

@dp.message_handler(text='Диплом')
async def send_welcome(message: types.Message):
    await message.answer("Пришлите Тему", reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id, message.text)

@dp.message_handler(text='Реферат')
async def send_welcome(message: types.Message):
    await message.answer("Пришлите Тему", reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id, message.text)

@dp.message_handler(content_types=['text'])
async def send_welcome(message: types.Message):
    await message.answer("Пришлите файл с требованиями (.doc)")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
