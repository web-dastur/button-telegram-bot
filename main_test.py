from aiogram import Bot, Dispatcher, executor, types
import logging
import random

from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from main_test_keybord import rkm, rkm_in, rkm_in_in

API_TOKEN = "6165032302:AAG7fEVOo7JizJl5LReQK-a_e44oE2v3Mh8"

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot = bot)

HELP_COMMAND = """
<b>/start</b> <em> Botni ishga tushirish uchun. </em>
<b>/help</b> <em> Yordam kerak bo'lganida .</em>
<b>/description</b> <em> Bot haqida qisqacha tarif.</em>
<b>/location</b> <em> Locatsiyani ko'rish uchun. </em>
"""

PHOTOS_URL = [

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7lgw7PcgKlkeMseBIZsrioioVcXeKfSvXnA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkvO-ZitgIS3lkq8QiC08TVXzactmcN4R03A&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrFguQkFXRztnrB_m1KHKYaTkraqznz_wcvA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2s0b7SFPS1eax0pUvbIJhlf3YqDM1SHh1lw&usqp=CAU"
]
PHOTOS_ = dict(zip(PHOTOS_URL,['Python programming language',
                              "Java programming language",
                              "Java_Script programming language",
                              "Go programming language"]))

PHOTOS_URL_FRONT = [

    "https://1.bp.blogspot.com/-2nzDotze7p4/YKzLqd34bzI/AAAAAAAABPc/ZUEnQ9OYZdMF0L31VkuBhD5vXSqkHlW6wCLcBGAsYHQ/s16000/HTML%2BFull%2BForm%2B%2528www.tutorialsmate.com%2529.png",
    "https://itproger.com/img/courses/1476977488.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfnG3cjdsLZZ4XcwP0cHVHmmV9KMPKf-iW7Q&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuxSDmJMtZP2ahJFst45QhhokrySddnNskDg&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSY5zQQfgYdauP902KBIcvqGVfUGvUT4gyCJw&usqp=CAU"
]

PHOTOS_FRONT = dict(zip(PHOTOS_URL_FRONT,['HTML - HyperText Markup Language ',
                              "CSS - Cascading Style Sheet",
                              "Java_Script programming language",
                              "Bootstrap ",
                              "React JS"]))

logging.basicConfig(level = logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer(text="👩‍💻 Assalomu Alaykum bizning botimizga xush kelibsiz.",reply_markup=rkm)
    await message.delete()


@dp.message_handler(Text(equals="⚙️help"))
async def help(message:types.Message):
    await message.answer(HELP_COMMAND,parse_mode="HTML")
    await message.delete()


@dp.message_handler(Text(equals="🌍location"))
async def location(message:types.Message):
    await bot.send_location(chat_id=message.chat.id,latitude=38.8582545, longitude=65.7917976)
    await message.delete()


@dp.message_handler(Text(equals='🔎description'))
async def description(message:types.Message):
    await message.answer("<b>👩‍💻Bu telegram bot hali ko'p funksiyaga ega emas</b>",parse_mode='HTML')
    await message.delete()


@dp.message_handler(Text(equals='🏞️Frontend'))
async def front_photo(message:types.Message):
    await message.answer(text='Frontend photo',
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Random",
                         reply_markup=rkm_in)



@dp.message_handler(Text(equals="®️ Random"))
async def photo_fron(message:types.Message):
    random_choice = random.choice(list(PHOTOS_FRONT.keys()))
    await message.answer_photo(photo=random_choice,
                               caption=PHOTOS_FRONT[random_choice],
                               reply_markup=rkm_in)
    await message.delete()
@dp.message_handler(Text(equals="⏭️ Back"))
async def back(message:types.Message):
    await message.answer(text="back to home", reply_markup=rkm)



@dp.message_handler(Text(equals='🛠️Backend'))
async def backend_photo(message:types.Message):
    await message.answer(text="Backend photo",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Random",reply_markup=rkm_in_in)
    await message.delete()

@dp.message_handler(Text(equals="®️ - Random"))
async def photo_fron(message:types.Message):
    choice = random.choice(list(PHOTOS_.keys()))
    await message.answer_photo(photo=choice,
                               caption=PHOTOS_[choice],
                               reply_markup=rkm_in_in)
    await message.delete()
@dp.message_handler(Text(equals="⏭️ Back"))
async def back(message:types.Message):
    await message.answer(text="back to home", reply_markup=rkm)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)

