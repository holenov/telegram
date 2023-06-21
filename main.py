from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('5668681697:AAFmEaLUsUToVJ7z5eohPWzT0zOKL5fDJSY')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://holenov.github.io/telegram/')))
    await message.answer('Здарова, заебал', reply_markup=markup)


executor.start_polling(dp)