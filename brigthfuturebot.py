from ctypes import c_int16

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup

bot = telebot.TeleBot("8782374872:AAE4KgJcp0JzHYFKoBHLreS1nx7HuYenmEE")
user_step = {}
admin_id = 7830634838
user_lang = {}
user_map = {}
bot.set_my_description("Bu bot orqali siz Bright Future haqida ma'lumot olishingiz mumkin")

uz1 = (
        " Bizning kurslar :\n"
        "- SAT\n"
        "- Tarix\n"
        "- Fizika\n"
        "- Kimyo\n"
        "- Rus tili\n"
        "- Biologiya\n"
        "- Ingliz tili\n"
        "- Koreys tili\n"
        "- Dasturlash\n"
        "- Matematika\n"
        "- Mental arifmetika\n"
        "- Ona tili-Adabiyot\n"
        "- Prezident maktabiga tayyorlov kurslari"
    )

uz2 = (
        " Бизнинг курслар :\n"
        "- SAT\n"
        "- Тарих\n"
        "- Физика\n"
        "- Кимё\n"
        "- Рус тили\n"
        "- Биология\n"
        "- Инглиз тили\n"
        "- Корейс тили\n"
        "- Дастурлаш\n"
        "- Математика\n"
        "- Ментал арифметика\n"
        "- Она тили-Адабиёт\n"
        "- Президент мактабига тайёрлов курслари"
    )

ru = (
        " Наши курсы :\n"
        "- SAT\n"
        "- История\n"
        "- Физика\n"
        "- Химия\n"
        "- Русский язык\n"
        "- Биология\n"
        "- Английский язык\n"
        "- Корейский язык\n"
        "- Программирование\n"
        "- Математика\n"
        "- Ментальная арифметика\n"
        "- Родной язык и литература\n"
        "- Подготовка в Президентские школы"
    )

en = (
        " Our courses :\n"
        "- SAT\n"
        "- History\n"
        "- Physics\n"
        "- Chemistry\n"
        "- Russian language\n"
        "- Biology\n"
        "- English language\n"
        "- Korean language\n"
        "- Programming\n"
        "- Mathematics\n"
        "- Mental arithmetic\n"
        "- Native language and literature\n"
        "- Preparation for Presidential schools"
    )










@bot.message_handler(commands=['start'])
def start(message):
    btn = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz1")
    btn2 = InlineKeyboardButton(text="🇺🇿 Ўзбекча", callback_data="uz2")
    btn3 = InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
    btn4 = InlineKeyboardButton(text="🇺🇸 English", callback_data="en")

    btn.add(btn1, btn2, btn3, btn4)

    text = (
        "O'zingizga qulay tilni tanlang 🇺🇿\n\n"
        "Ўзингизга қулай тилни танланг 🇺🇿\n\n"
        "Выбери язык, который тебе нравится 🇷🇺\n\n"
        "Choose the language you like 🇺🇸"
    )

    bot.reply_to(message, text, reply_markup=btn)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_id = call.message.chat.id
    if call.data == "uz1":

        user_lang[user_id] = "uz"
        a = ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = KeyboardButton("Brigth Future haqida!")
        a2 = KeyboardButton("sozlamalar")
        a3= KeyboardButton("bot haqida")
        a4 = KeyboardButton("Brigth Future ishtimoiy tarmoqlari")
        a5 = KeyboardButton("Admin ")
        a.add(a1, a2, a3, a4,a5)







        bot.send_message(call.message.chat.id, "Siz O'zbek tilini tanladingiz",reply_markup=a)
    elif call.data == "uz2":
        user_lang[user_id] = "uzc"
        b = ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = KeyboardButton("Brigth Future Ҳақида!")
        b2 = KeyboardButton("Созламалар")
        b3 = KeyboardButton("Бот ҳақида")
        b4 = KeyboardButton("Brigth Future Ижтимоий тармоқлари")
        b5 = KeyboardButton("Админ")
        b.add(b1, b2, b3, b4,b5)
        bot.send_message(call.message.chat.id, "Сиз ўзбек тилини танладингиз",reply_markup=b)

    elif call.data == "ru":
        user_lang[user_id] = "ru"
        c = ReplyKeyboardMarkup(resize_keyboard=True)
        c1 = KeyboardButton("Brigth Future О нас")
        c2 = KeyboardButton("Настройки")
        c3 = KeyboardButton("О боте")
        c4 = KeyboardButton("Brigth Future Социальные сети")
        c5 = KeyboardButton("админ")
        c.add(c1, c2, c3, c4,c5)
        bot.send_message(call.message.chat.id, "Вы выбрали русский язык",reply_markup=c)




    elif call.data == "en":
        user_lang[user_id] = "en"
        d = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Brigth Future about")
        d2 = KeyboardButton("setting")
        d3 = KeyboardButton("About the bot")
        d4 = KeyboardButton("Brigth Future Social media")
        d5 = KeyboardButton("admin")
        d.add(d1, d2, d3,d4,d5)
        bot.send_message(call.message.chat.id, "You selected English",reply_markup=d)


@bot.message_handler(func=lambda message : True )
def keyboard(message):
    n ="Nomer : 55-202-73-73\nInstagram : bright_future.asaka\nTelegram : @Bright_future_asaka "
    if message.text =="Brigth Future haqida!":

        bot.send_message(message.chat.id,f"{uz1}")
    elif message.text =="sozlamalar":
        q = ReplyKeyboardMarkup(resize_keyboard=True)
        q1 =KeyboardButton("Tilni ozgartirish")
        back = KeyboardButton("Orqaga")
        q.add(q1,back)

        bot.send_message(message.chat.id,"Nima qilmoq chisiz",reply_markup=q)
    elif message.text =="Orqaga":
        m = ReplyKeyboardMarkup(resize_keyboard=True)
        m1 =['Brigth Future haqida!','sozlamalar','bot haqida',"Brigth Future ishtimoiy tarmoqlari",'Admin']
        m.add(*[KeyboardButton(item)for item in m1])
        bot.send_message(message.chat.id,"asosiy menyu",reply_markup=m)
    elif message.text == "Tilni ozgartirish":
        btn = InlineKeyboardMarkup(row_width=2)

        btn1 = InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz1")
        btn2 = InlineKeyboardButton(text="🇺🇿 Ўзбекча", callback_data="uz2")
        btn3 = InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
        btn4 = InlineKeyboardButton(text="🇺🇸 English", callback_data="en")

        btn.add(btn1, btn2, btn3, btn4)

        text = (
            "O'zingizga qulay tilni tanlang 🇺🇿\n\n"
            "Ўзингизга қулай тилни танланг 🇺🇿\n\n"
            "Выбери язык, который тебе нравится 🇷🇺\n\n"
            "Choose the language you like 🇺🇸"
        )

        bot.reply_to(message, text, reply_markup=btn)

    elif message.text =="bot haqida":
        bot.send_message(message.chat.id,"Bu bot orqali siz Brigth Future haqida malumot olishingiz majud")
    elif message.text =="Brigth Future ishtimoiy tarmoqlari":
        bot.send_message(message.chat.id,f"{n}")
    elif message.text =="Admin":
        bot.send_message(message.chat.id,"Admn : @Muhammadjon2202 ")






    elif message.text =="Brigth Future Ҳақида!":
        bot.send_message(message.chat.id,f"{uz2}")
    elif message.text =="Созламалар":
        q = ReplyKeyboardMarkup(resize_keyboard=True)
        q1 =KeyboardButton("Тилни ўзгартириш")
        back = KeyboardButton("orqaga")
        q.add(q1,back)
        bot.send_message(message.chat.id,"Нима қилмоқчисиз",reply_markup=q)
    elif message.text =="orqaga":
        m = ReplyKeyboardMarkup(resize_keyboard=True)
        m1 = [
            'Brigth Future Ҳақида!',
            'Созламалар',
            'Бот ҳақида',
            'Brigth Future Ижтимоий тармоқлари',
            'Админ'
        ]
        m.add(*[KeyboardButton(item) for item in m1])
        bot.send_message(message.chat.id,"Асосий меню",reply_markup=m)
    elif message.text == "Тилни ўзгартириш":
        btn = InlineKeyboardMarkup(row_width=2)

        btn1 = InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz1")
        btn2 = InlineKeyboardButton(text="🇺🇿 Ўзбекча", callback_data="uz2")
        btn3 = InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
        btn4 = InlineKeyboardButton(text="🇺🇸 English", callback_data="en")

        btn.add(btn1, btn2, btn3, btn4)

        text = (
            "O'zingizga qulay tilni tanlang 🇺🇿\n\n"
            "Ўзингизга қулай тилни танланг 🇺🇿\n\n"
            "Выбери язык, который тебе нравится 🇷🇺\n\n"
            "Choose the language you like 🇺🇸"
        )

        bot.reply_to(message, text, reply_markup=btn)
    elif message.text =="Бот ҳақида":
        bot.send_message(message.chat.id,"Бу бот орқали сиз Brigth Future ҳақида маълумот олишингиз мумкин")
    elif message.text =="Brigth Future Ижтимоий тармоқлари":
        bot.send_message(message.chat.id,f"{n}")
    elif message.text =="Админ":
        bot.send_message(message.chat.id,"Админ :@Muhammadjon2202 ")





    elif message.text =="Brigth Future О нас":
        bot.send_message(message.chat.id,f"{ru}")
    elif message.text =="Настройки":
        q = ReplyKeyboardMarkup(resize_keyboard=True)
        q1 =KeyboardButton("Сменить язык")
        back = KeyboardButton("Назад")
        q.add(q1,back)
        bot.send_message(message.chat.id,"Что вы хотите сделать?",reply_markup=q)
    elif message.text ==    "Назад":
        m = ReplyKeyboardMarkup(resize_keyboard=True)
        m1 = [
            'Brigth Future О нас',
            'Настройки',
            'О боте',
            'Brigth Future Социальные сети',
            'админ'
        ]
        m.add(*[KeyboardButton(item) for item in m1])

        bot.send_message(message.chat.id,"Главное меню",reply_markup=m)
    elif message.text == "Сменить язык":
        btn = InlineKeyboardMarkup(row_width=2)

        btn1 = InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz1")
        btn2 = InlineKeyboardButton(text="🇺🇿 Ўзбекча", callback_data="uz2")
        btn3 = InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
        btn4 = InlineKeyboardButton(text="🇺🇸 English", callback_data="en")

        btn.add(btn1, btn2, btn3, btn4)

        text = (
            "O'zingizga qulay tilni tanlang 🇺🇿\n\n"
            "Ўзингизга қулай тилни танланг 🇺🇿\n\n"
            "Выбери язык, который тебе нравится 🇷🇺\n\n"
            "Choose the language you like 🇺🇸"
        )

        bot.reply_to(message, text, reply_markup=btn)
    elif message.text =="О боте":
        bot.send_message(message.chat.id,"Через этого бота вы можете получить информацию о Brigth Future")
    elif message.text =="Brigth Future Социальные сети":
        bot.send_message(message.chat.id, f"{n}")
    elif message.text == "админ":
        bot.send_message(message.chat.id,"админ : @Muhammadjon2202 ")




    elif message.text =="Brigth Future about":
        bot.send_message(message.chat.id,f"{en}")
    elif message.text =="setting":
        q = ReplyKeyboardMarkup(resize_keyboard=True)
        q1 =KeyboardButton("Change language")
        back = KeyboardButton("Back")
        q.add(q1,back)
        bot.send_message(message.chat.id,"What do you want to do?",reply_markup=q)
    elif message.text =="Back":
        m = ReplyKeyboardMarkup(resize_keyboard=True)
        m1 = [
            'Brigth Future about',
            'setting',
            'About the bot',
            'Brigth Future Social media',
            'admin'
        ]
        m.add(*[KeyboardButton(item) for item in m1])
        bot.send_message(message.chat.id,"Main menu",reply_markup=m)
    elif message.text == "Change language":
        btn = InlineKeyboardMarkup(row_width=2)

        btn1 = InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz1")
        btn2 = InlineKeyboardButton(text="🇺🇿 Ўзбекча", callback_data="uz2")
        btn3 = InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
        btn4 = InlineKeyboardButton(text="🇺🇸 English", callback_data="en")

        btn.add(btn1, btn2, btn3, btn4)

        text = (
            "O'zingizga qulay tilni tanlang 🇺🇿\n\n"
            "Ўзингизга қулай тилни танланг 🇺🇿\n\n"
            "Выбери язык, который тебе нравится 🇷🇺\n\n"
            "Choose the language you like 🇺🇸"
        )

        bot.reply_to(message, text, reply_markup=btn)
    elif message.text =="About the bot":
        bot.send_message(message.chat.id,"Through this bot, you can get information about Brigth Future")
    elif message.text =="Brigth Future Social media":
        bot.send_message(message.chat.id, f"{n}")
    elif message.text =="admin":
        bot.send_message(message.chat.id,"admin: @Muhammadjon2202 ")




















bot.infinity_polling()