from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
from aiogram.filters.command import Command

API_TOKEN = '7060030383:AAHPgrlOgGXBxXL31_N1ztmli_yYsz1SSQE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Ты идиот? сразу надо было айограмом пользоваться, но всё же вот доступ к моему новенькому телеграмм каналу, в котором ты можешь делать всё что угодно!! (потому что ты и являешься владельцем) https://t.me/+lgnzFvBJBYZhM2Fi")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


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


@dp.message(Command("/Hello"))
async def cmd_test1(message: types.Message):
    await message.reply("Ты лох")

@dp.message(Command("/qwe"))
async def cmd_test2(message: types.Message):
    await message.reply("Привет пупсик")


















































































