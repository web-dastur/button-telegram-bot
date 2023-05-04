from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

rkm = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,
                          input_field_placeholder="Enter your message",
                          selective=True)
button = KeyboardButton("/start")
button1 = KeyboardButton("⚙️help")
button2 = KeyboardButton("🔎description")
button3 = KeyboardButton("🌍location")
button4 = KeyboardButton("🏞️Frontend")
button5 = KeyboardButton("🛠️Backend")
rkm.add(button, button1,button2,button3,button4,button5)

rkm_in = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,
                          input_field_placeholder="Enter your message",
                          selective=True)
rkm_in_in = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,
                          input_field_placeholder="Enter your message",
                          selective=True)
btn1 = KeyboardButton("®️ - Random")
btn = KeyboardButton("®️ Random")
btn_2 = KeyboardButton("⏭️ Back")
rkm_in.add(btn,btn_2)
rkm_in_in.add(btn1,btn_2)