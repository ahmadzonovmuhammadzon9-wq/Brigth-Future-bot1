from ctypes import c_int16

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup

bot = telebot.TeleBot("8782374872:AAE4KgJcp0JzHYFKoBHLreS1nx7HuYenmEE")
user_step = {}
admin_id = 7830634838
user_lang = {}
user_map = {}
bot.set_my_description("Bu bot orqali siz Bright Future haqida ma'lumot olishingiz mumkin")

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
    if call.data == "uz1":
        a = ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = KeyboardButton("Brigth Future haqida!")
        a2 = KeyboardButton("sozlamalar")
        a3= KeyboardButton("bot haqida")
        a4 = KeyboardButton("Brigth Future ishtimoiy tarmoqlari")
        a5 = KeyboardButton("Admin bilan aloqa ")
        a.add(a1, a2, a3, a4,a5)







        bot.send_message(call.message.chat.id, "Siz O'zbek tilini tanladingiz",reply_markup=a)
    elif call.data == "uz2":
        b = ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = KeyboardButton("Brigth Future Ҳақида!")
        b2 = KeyboardButton("Созламалар")
        b3 = KeyboardButton("Бот ҳақида")
        b4 = KeyboardButton("Brigth Future Ижтимоий тармоқлари")
        b5 = KeyboardButton("Админ билан алоқа")
        b.add(b1, b2, b3, b4,b5)
        bot.send_message(call.message.chat.id, "Сиз ўзбек тилини танладингиз",reply_markup=b)

    elif call.data == "ru":
        c = ReplyKeyboardMarkup(resize_keyboard=True)
        c1 = KeyboardButton("Brigth Future О нас")
        c2 = KeyboardButton("Настройки")
        c3 = KeyboardButton("О боте")
        c4 = KeyboardButton("Brigth Future Социальные сети")
        c5 = KeyboardButton("Связаться с админом")
        c.add(c1, c2, c3, c4,c5)
        bot.send_message(call.message.chat.id, "Вы выбрали русский язык",reply_markup=c)




    elif call.data == "en":
        d = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Brigth Future about")
        d2 = KeyboardButton("setting")
        d3 = KeyboardButton("About the bot")
        d4 = KeyboardButton("Brigth Future Social media")
        d5 = KeyboardButton("Contact admin")
        d.add(d1, d2, d3,d4,d5)
        bot.send_message(call.message.chat.id, "You selected English",reply_markup=d)


@bot.message_handler(func=lambda message : True )
def keyboard(message):
    if message.text =="Brigth Future haqida!":
        bot.send_message(message.chat.id,"Bizda IT,Ingliz tili va boshqa til va sohalar bor")
    elif message.text =="sozlamalar":
        q = ReplyKeyboardMarkup(resize_keyboard=True)
        q1 =KeyboardButton("Tilni ozgartirish")
        back = KeyboardButton("Orqaga")
        q.add(q1,back)
        bot.send_message(message.chat.id,"Nima qilmoq chisiz",reply_markup=q)
    elif message.text == "Tilni ozgartirish":
        bot.send_message(message.chat.id,"Tilni ozgartirish funksiyasi hali mavjud emas")
    elif message.text =="bot haqida":
        bot.send_message(message.chat.id,"Bu bot orqali siz Brigth Future haqida malumot olishingiz majud")
    elif message.text =="Brigth Future ishtimoiy tarmoqlari":
        bot.send_message(message.chat.id,"Nomer:   \nInstagram:   ")
    elif message.text =="Admin bilan aloqa":
        user_step[message.chat.id] = "write_to_admin"

        bot.send_message(message.chat.id, "Xabaringizni yozing ")

        return
    if user_step.get(message.chat.id) == "write_to_admin":
        user_step[message.chat.id] = None

        sent = bot.send_message(
            admin_id,
            f" Yangi xabar\n\n{message.text}"
        )

        user_map[sent.message_id] = message.chat.id

        bot.send_message(message.chat.id, "Xabaringiz yuborildi ")



    elif message.text =="Brigth Future Ҳақида!":
        bot.send_message(message.chat.id,"Kirillcha: Бизда IT, инглиз тили ва бошқа тил ва соҳалар бор")
    elif message.text =="Созламалар":
        q = ReplyKeyboardMarkup(resize_keyboard=True)
        q1 =KeyboardButton("Тилни ўзгартириш")
        back = KeyboardButton("Orqaga")
        q.add(q1,back)
        bot.send_message(message.chat.id,"Нима қилмоқчисиз",reply_markup=q)
    elif message.text == "Тилни ўзгартириш":
        bot.send_message(message.chat.id,"Тилни ўзгартириш функцияси ҳали мавжуд эмас")
    elif message.text =="Бот ҳақида":
        bot.send_message(message.chat.id,"Бу бот орқали сиз Brigth Future ҳақида маълумот олишингиз мумкин")
    elif message.text =="Brigth Future Ижтимоий тармоқлари":
        bot.send_message(message.chat.id,"Nomer:   \nInstagram:   ")
    elif message.text =="Админ билан алоқа":
        user_step[message.chat.id] = "write_to_admin"
        bot.send_message(message.chat.id,"Хабарингизни ёзинг")
    if user_step.get(message.chat.id) == "write_to_admin":
        user_step[message.chat.id] = None

        sent = bot.send_message(
            admin_id,
            f"Yangi xabar\n\n{message.text}"
        )

        user_map[sent.message_id] = message.chat.id

        bot.send_message(message.chat.id, "Xabaringiz yuborildi ")




    elif message.text =="Brigth Future О нас":
        bot.send_message(message.chat.id,"У нас есть IT, английский язык и другие языки и направления")
    elif message.text =="Настройки":
        q = ReplyKeyboardMarkup(resize_keyboard=True)
        q1 =KeyboardButton("Сменить язык")
        back = KeyboardButton("Назад")
        q.add(q1,back)
        bot.send_message(message.chat.id,"Что вы хотите сделать?",reply_markup=q)
    elif message.text == "Сменить язык":
        bot.send_message(message.chat.id,"Функция смены языка пока недоступна")
    elif message.text =="О боте":
        bot.send_message(message.chat.id,"Через этого бота вы можете получить информацию о Brigth Future")
    elif message.text =="Brigth Future Социальные сети":
        bot.send_message(message.chat.id,"Nomer:   \nInstagram:   ")
    elif message.text =="Связаться с админом":
        user_step[message.chat.id] = "write_to_admin"
        bot.send_message(message.chat.id,"Напишите ваше сообщение")

    if user_step.get(message.chat.id) == "write_to_admin":
        user_step[message.chat.id] = None

        sent = bot.send_message(
            admin_id,
            f" Yangi xabar\n\n{message.text}"
        )

        user_map[sent.message_id] = message.chat.id

        bot.send_message(message.chat.id, "Xabaringiz yuborildi ")



    elif message.text =="Brigth Future about":
        bot.send_message(message.chat.id,"We have IT, English language, and other languages and fields")
    elif message.text =="setting":
        q = ReplyKeyboardMarkup(resize_keyboard=True)
        q1 =KeyboardButton("Change language")
        back = KeyboardButton("Back")
        q.add(q1,back)
        bot.send_message(message.chat.id,"What do you want to do?",reply_markup=q)
    elif message.text == "Change language":
        bot.send_message(message.chat.id,"The language change feature is not available yet")
    elif message.text =="About the bot":
        bot.send_message(message.chat.id,"Through this bot, you can get information about Brigth Future")
    elif message.text =="Brigth Future Social media":
        bot.send_message(message.chat.id,"Nomer:   \nInstagram:   ")

    elif message.text =="Contact admin":
        user_step[message.chat.id] = "write_to_admin"
        bot.send_message(message.chat.id,"Write your message")

    if user_step.get(message.chat.id) == "write_to_admin":
        user_step[message.chat.id] = None


        sent = bot.send_message(
            admin_id,
            f" Yangi xabar\n\n{message.text}"
        )


        user_map[sent.message_id] = message.chat.id

        bot.send_message(message.chat.id, "Xabaringiz yuborildi ")




@bot.message_handler(func=lambda message: message.chat.id == admin_id)
def admin_reply(message):
    try:
        if message.reply_to_message:

            msg_id = message.reply_to_message.message_id

            if msg_id in user_map:
                user_id = user_map[msg_id]

                lang = user_lang.get(user_id)

                if lang == "uz":
                    text = f" Admin javobi:\n{message.text}"
                elif lang == "uzc":
                    text = f" Админ жавоби:\n{message.text}"
                elif lang == "ru":
                    text = f" Ответ администратора:\n{message.text}"
                elif lang == "en":
                    text = f"Admin reply:\n{message.text}"
                else:
                    text = message.text

                bot.send_message(user_id, text)

        else:
            bot.send_message(admin_id, " User xabariga reply qiling!")

    except Exception as e:
        bot.send_message(admin_id, f"Xatolik: {e}")
















bot.infinity_polling()