from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

API_TOKEN = '6976928515:AAGzaDknisN3ohTapwFHCK5A0_m7GeVmJP8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! чтобы писать команды используй приписку / перед твоим сообщением. Для помощи введи /help. для перехода в мой новенький телеграм канал нажми [здесь](https://t.me/+lgnzFvBJBYZhM2Fi)", parse_mode="Markdown", disable_web_page_preview=True)

async def main():
    await dp.start_polling(bot)


@dp.message(Command(commands =["hello"]))
async def cmd_test1(message: types.Message):
    await message.reply("Папа привет, сделай пожалуйста эмоцию сигмы слово пацана!!!")

@dp.message(Command("help"))
async def cmd_test2(message: types.Message):
    await message.reply("Все доступные команды в данном боте: /pasxalko1, /pasxalko2, /pasxalko3, /pasxalko4, /pasxalko5, /xz, /random_number, /random, /toilet, /films, /videos, /wikipedia, /help, /hello, /lebron, /gay, /telegram_piton_govno")

@dp.message(Command(commands =["gay"]))
async def cmd_test3(message: types.Message):
    await message.reply("no)")

@dp.message(Command(commands =["telegram_piton_govno"]))
async def cmd_test4(message: types.Message):
    await message.reply("нажми [здесь](https://t.me/+lgnzFvBJBYZhM2Fi)", parse_mode="Markdown", disable_web_page_preview=True)

@dp.message(Command(commands =["lebron"]))
async def cmd_test5(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo=FSInputFile('./леброн.webp'), caption="You are my sunshine... my only sunshine...")

@dp.message(Command(commands =["films"]))
async def cmd_test6(message: types.Message):
    await message.reply("хз зачем тебе ссылка на рандомные фильмы но [вот](http://castlots.org/sluchajnyj-film/)", parse_mode="Markdown", disable_web_page_preview=True)

@dp.message(Command(commands =["videos"]))
async def cmd_test7(message: types.Message):
    await message.reply("случайное видео на ютубе? [ну ок](https://www.youtube-tech.ru/random-pick/random-video/)", parse_mode="Markdown", disable_web_page_preview=True)

@dp.message(Command(commands =["wikipedia"]))
async def cmd_test8(message: types.Message):
    await message.reply("рандомная статья на википедии? [легко](https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0)", parse_mode="Markdown", disable_web_page_preview=True)

@dp.message(Command(commands =["xz"]))
async def cmd_test9(message: types.Message):
    await message.reply("ti xotel skazat KZ?)))")

@dp.message(Command(commands =["random_number"]))
async def cmd_test10(message: types.Message):
    await message.reply("рандомное число от 1 до 100? Хм наверно [52](https://www.random.org/)", parse_mode="Markdown", disable_web_page_preview=True)

@dp.message(Command(commands =["random"]))
async def cmd_test11(message: types.Message):
    await message.reply("бро итс джаст рандомный [генератор](https://randomall.ru/custom/gen/random?id=5098)", parse_mode="Markdown", disable_web_page_preview=True)

@dp.message(Command(commands =["toilet"]))
async def cmd_test12(message: types.Message):
    await message.reply("[какой ты скебеде тоалет?](https://randomall.ru/custom/gen/9727)", parse_mode="Markdown", disable_web_page_preview=True)

@dp.message(Command(commands =["pasxalko1"]))
async def cmd_test13(message: types.Message):
    await message.reply("махабатпыяласын")

@dp.message(Command(commands =["pasxalko2"]))
async def cmd_test14(message: types.Message):
    await message.reply("я фсё патирял фсё патирял...")

@dp.message(Command(commands =["pasxalko3"]))
async def cmd_test15(message: types.Message):
    await message.reply("52")

@dp.message(Command(commands =["pasxalko4"]))
async def cmd_test16(message: types.Message):
    await message.reply("да здравствует Санкт-Петербург и этот город наш")

@dp.message(Command(commands =["pasxalko5"]))
async def cmd_test17(message: types.Message):
    await message.reply("пасхалка 3 и 4 дополняют друг друга)")

@dp.message()
async def cmd_test3(message: types.Message):
    await message.reply("я не знаю такую команду")

if __name__ == "__main__":
    asyncio.run(main())
    
#я в полной комнате но я совсем один
#вокруг меня модели как с картин
#я не ищу среди них половин
#сердце - как лёд, бытие - лабиринт

#мой отец ушёл когда мне было только 5 месяцев
#я хотел повеситься когда исполнилось 10
#и моя мать сошла с ума когда мне было 14
#почти все мои друзья сидят, как я смог выбраться?

#мысли намного глубже чем просто деньги 
#что вокруг меня? неужели я удобрение?
#это не любовь - это просто трение
#творчество сильнее выгоды, мировозрения

#быть против власти - не значит быть против родины
#я люблю Россию за запах чёрной смородины
#не дам русофобам нажиться на моих взглядах
#я в золотистых полях и колосьях, ляг со мной рядом

#мой отец ушёл когда мне было только 5 месяцев
#я хотел повеситься когда исполнилось 10
#и моя мать сошла с ума когда мне было 14
#почти все мои друзья сидят, как я смог выбраться?