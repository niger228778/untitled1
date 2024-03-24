from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
from aiogram.filters.command import Command

API_TOKEN = '7060030383:AAHPgrlOgGXBxXL31_N1ztmli_yYsz1SSQE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! чтобы писать команды используй приписку / перед твоим сообщением. Для помощи введи /help. для перехода в мой новенький телеграм канал нажми [здесь](https://t.me/+lgnzFvBJBYZhM2Fi)", parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)




def catalog (msg):
    pass
def buy (msg):
    pass
def handler (message):
    links = {
        'Привет пупс': catalog,
        'Ты лох': buy
    }

    if not message.text in links:
        message.answer('Я хз чё ты хочешь')
        return
    links[message.text](message)


@dp.message(Command(commands =["Hello"]))
async def cmd_test1(message: types.Message):
    await message.reply("Папа привет, сделай сделай пожалуйста эмоцию сигмы слово пацана!!!")

@dp.message(Command("help"))
async def cmd_test2(message: types.Message):
    await message.reply("Все доступные команды в данном боте: /help, /Hello, /How_are_you, /telegram_piton_govno")

@dp.message(Command(commands =["How are you"]))
async def cmd_test3(message: types.Message):
    await message.reply("У меня всё нормально. А у тебя как? Мне всё равно пофиг))")

@dp.message(Command(commands =["telegram_piton_govno"]))
async def cmd_test4(message: types.Message):
    await message.reply("нажми [здесь](https://t.me/+lgnzFvBJBYZhM2Fi)", parse_mode="Markdown")


if __name__ == "__main__":
    asyncio.run(main())











































































