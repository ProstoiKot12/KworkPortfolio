
from aiogram import Bot, Dispatcher, executor, types
import config
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
TOKEN = 'token'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


ras = KeyboardButton('📝 Расписание')
els = InlineKeyboardButton('Нажми сюда', url='https://elschool.ru/Logon/Index')
el = KeyboardButton('📖 Электронный дневник')
sr_bal = KeyboardButton('🔢 Средний бал')

but1 = KeyboardButton('Понедельник ')
but2 = KeyboardButton('Вторник ')
but3 = KeyboardButton('Среда ')
but4 = KeyboardButton('Четверг ')
but5 = KeyboardButton('Пятница ')
but6 = KeyboardButton('Суббота ')

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb1.row(but1, but4)
kb1.add(but2, but5)
kb1.add(but3, but6)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb2.add(ras, el, sr_bal)

kb3 = InlineKeyboardMarkup()
kb3.add(els)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name} я бот помощник, ты можешь вызвать меню /menu", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['menu'])
async def send_menu(message: types.Message):
    await message.answer('Просто выбери то что тебе надо', reply_markup=kb2)

@dp.message_handler(text= 'Понедельник')
async def send_welcome(message: types.Message):
    await message.answer('Вот расписание на ужасный понедельник:\n'
                                          "\n"
                                        "1	Изо\n"
                                        "2	Англ яз\n"
                                        "3	Физра\n"
                                        "4	Алгебра\n"
                                        "5	Икт\n"
                                        "6	Рус яз\n"
                                        "7	Доп. матем\n ")

@dp.message_handler(text= 'Вторник')
async def send_welcome(message: types.Message):
    await message.answer('Вот расписание на такой себе вторник:\n'
                                          "\n"
                                        "1	Истроия\n"
                                        "2	Физра\n"
                                        "3	Химия\n"
                                        "4	Немецкий\n"
                                        "5	Литература\n"
                                        "6	Геометрия\n"
                                        "7	Кл час\n ")

@dp.message_handler(text= 'Среда')
async def send_welcome(message: types.Message):
    await message.answer('Вот расписание на среднию среду:\n'
                                          "\n"
                                        "1	Физика\n"
                                        "2	Англ яз\n"
                                        "3	Биология\n"
                                        "4	Рус яз\n"
                                        "5	Алгебра\n"
                                        "6	География\n")

@dp.message_handler(text= 'Четверг')
async def send_welcome(message: types.Message):
    await message.answer('Вот расписание на сложний четверг:\n'
                                        "\n"
                                        "1	Литер\n"
                                        "2	Биология\n"
                                        "3	Рус яз\n"
                                        "4	Геометрия\n"
                                        "5	Химия\n"
                                        "6	Общество\n  ")

@dp.message_handler(text= 'Пятница')
async def send_welcome(message: types.Message):
    await message.answer('Вот расписание на отличную пятницу:\n'
                                          "\n"
                                        "1	Алгебра\n"
                                        "2	Рус яз\n"
                                        "3	Родной\n"
                                        "4	Баш/ИКБ\n"
                                        "5	ОБЖ\n"
                                        "6	История\n"
                                        "7	Технология\n ")

@dp.message_handler(text= 'Суббота')
async def send_welcome(message: types.Message):
    await message.answer('В субботу выходной так что, отдыхай')

@dp.message_handler(text= 'Спасибо')
async def send_welcome(message: types.Message):
    await message.answer('Пожалуйста, приходи еще')

@dp.message_handler(text= 'Спасибо тебе')
async def send_welcome(message: types.Message):
    await message.answer('Это тебе спасибо, приходи еще')

@dp.message_handler(text= '📖 Электронный дневник')
async def send_welcome(message: types.Message):
    await message.reply('Электронный дневник', reply_markup=kb3)

@dp.message_handler(text= '📝 Расписание')
async def send_welcome(message: types.Message):
    await message.reply("Чтобы посмотреть расписание выбери день недели", reply_markup=kb1)

@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("Убираем шаблоны сообщений", reply_markup=ReplyKeyboardRemove())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
