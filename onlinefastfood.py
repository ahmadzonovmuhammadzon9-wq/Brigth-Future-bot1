import telebot
from pyexpat.errors import messages
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,  KeyboardButton, ReplyKeyboardMarkup



bot=telebot.TeleBot("8536005139:AAF5IJA66U-xw80I0N7GeGDZi4m-clTR7GY")
user={}
waiting={}
def main_manu():
    markup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    markup.add(
        KeyboardButton("📦 Mahsulotlar"),
        KeyboardButton("🧺 Savatchani ko'rish")
    )
    markup.add(
        KeyboardButton("📝 Buyurtmalarim"),
        KeyboardButton("💭 Fikr-mulohazalar")
    )
    markup.add(
        KeyboardButton("🎁 Aksiyalar"),
        KeyboardButton("👤 Profilim")
    )
    return markup
def mahsulotlar():
    key = InlineKeyboardMarkup(row_width=3)
    key.add(
        InlineKeyboardButton("🥪 Sandwich",callback_data='sandwich'),
        InlineKeyboardButton("🌭 Hotdog",callback_data='hotdog')
    )
    key.add(
        InlineKeyboardButton("🍿 KFS",callback_data='kfs'),
        InlineKeyboardButton("🍣 Sushi",callback_data='sushi')
    )
    key.add(
        InlineKeyboardButton("🍕 Pizza",callback_data='pizza'),
        InlineKeyboardButton("🥤 Ichimliklar",callback_data='ichimliklar')
    )
    return key

@bot.message_handler(commands=['start'])
def start(message):
    k=ReplyKeyboardMarkup(resize_keyboard=True)
    b=KeyboardButton(text="📞Raqamni ulashish", request_contact=True)
    k.add(b)
    bot.send_message(message.chat.id,"📞 Ro'yxatdan o'tish uchun raqamingizni kiriting yoki ulashing:",reply_markup=k)


@bot.message_handler(content_types=['contact'])
def contact(message):
    user_id = message.from_user.id
    phone = message.contact.phone_number


    user[user_id] = {
        "phone": phone,
        "name": message.from_user.first_name
    }


    bot.send_message(message.chat.id,"Ro'yxatdan muvaffaqiyatli o'tdingiz ✅",reply_markup=main_manu())


@bot.message_handler(func=lambda message: True)
def menu(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    phone = user[user_id]["phone"]
    if waiting.get(user_id):
        waiting[user_id] = False
        bot.send_message(message.chat.id, "💬 Fikringiz uchun rahmat! 🙏", reply_markup=main_manu())
        return
    if message.text == "📦 Mahsulotlar":

        bot.send_message(message.chat.id,"Menu🍽",reply_markup=mahsulotlar())

    elif message.text =="🧺 Savatchani ko'rish":
        bot.send_message(message.chat.id,"")

    elif message.text == "📝 Buyurtmalarim":
        bot.send_message(message.chat.id,"")

    elif message.text == "💭 Fikr-mulohazalar":
        waiting[user_id] = True
        bot.send_message(message.chat.id,"Fikr-mulohazangizni qoldiring:")


    elif message.text == "🎁 Aksiyalar":
        f1=open("promokod.jpg","rb")
        f2 =open("10persant.jpg","rb")
        f3=open("birthday.jpg","rb")



        bot.send_photo(message.chat.id,f1,
                         "1. Promo-kod: Habib12 - 45000 so'm chegirma\n 🎟 (90,000 so'mdan yuqori buyurtmalarda) ❗️")
        bot.send_photo(message.chat.id,f2, "2. 3 yoki undan ortiq mahsulotga 10% \nchegirma.🎁")
        bot.send_photo(message.chat.id,f3, "3. Tug'ilgan kuningizda maxsus sovg'a!🎉")
    elif message.text == "👤 Profilim":
        bot.send_message(message.chat.id,f"Sizning profilingiz:\nIsm:{user_name}\nID:{user_id}\nRaqam:{phone}")



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "sandwich":
        o=InlineKeyboardMarkup(row_width=3)
        o1=InlineKeyboardButton("➖",callback_data="-")
        o2=InlineKeyboardButton("0som",callback_data="hisob")
        o3=InlineKeyboardButton("➕",callback_data="+")
        o4=InlineKeyboardButton("🧺Savatga qoshish",callback_data="savat")
        o.add(o1,o2,o3,o4)
        s =open("sandwich.jpg","rb")
        bot.send_photo(call.message.chat.id,s,"Sandwich \nNarxi:17000",reply_markup=o)
    elif call.data == "hotdog":
        o = InlineKeyboardMarkup(row_width=3)
        o1 = InlineKeyboardButton("➖", callback_data="-1")
        o2 = InlineKeyboardButton("0som", callback_data="hisob1")
        o3 = InlineKeyboardButton("➕",callback_data="+1")
        o4=InlineKeyboardButton("🧺Savatga qoshish",callback_data="savat1")
        o.add(o1, o2, o3,o4)
        s =open("hotdog.jpg","rb")
        bot.send_photo(call.message.chat.id,s,"Hotdog\nNarxi:14000",reply_markup=o)
    elif call.data == "kfs":
        o = InlineKeyboardMarkup(row_width=3)
        o1 = InlineKeyboardButton("➖", callback_data="-2")
        o2 = InlineKeyboardButton("0som", callback_data="hisob2")
        o3 = InlineKeyboardButton("➕",callback_data="+2")
        o4=InlineKeyboardButton("🧺Savatga qoshish",callback_data="savat2")
        o.add(o1, o2, o3,o4)
        s =open("kfc.jpg","rb")
        bot.send_photo(call.message.chat.id,s,"KFC\nNarxi:15000",reply_markup=o)
    elif call.data == "sushi":
        o = InlineKeyboardMarkup(row_width=3)
        o1 = InlineKeyboardButton("➖", callback_data="-3")
        o2 = InlineKeyboardButton("0som", callback_data="hisob3")
        o3 = InlineKeyboardButton("➕",callback_data="+3")
        o4=InlineKeyboardButton("🧺Savatga qoshish",callback_data="savat3")
        o.add(o1, o2, o3,o4)
        s =open("sushi.jpg","rb")
        bot.send_photo(call.message.chat.id,s,"Sushi\nNarxi:30000",reply_markup=o)

    elif call.data == "pizza":
        o = InlineKeyboardMarkup(row_width=3)
        o1 = InlineKeyboardButton("➖", callback_data="-4")
        o2 = InlineKeyboardButton("0som", callback_data="hisob4")
        o3 = InlineKeyboardButton("➕",callback_data="+4")
        o4=InlineKeyboardButton("🧺Savatga qoshish",callback_data="savat4")
        o.add(o1, o2, o3,o4)
        s =open("ptsa1.jpg","rb")
        bot.send_photo(call.message.chat.id,s,"Pizza\nNarxi:60000",reply_markup=o)

    elif call.data == "ichimliklar":

        o=InlineKeyboardMarkup(row_width=3)
        o1=InlineKeyboardButton("🥤pepsi",callback_data="pepsi")
        o2=InlineKeyboardButton("🍷cola",callback_data="cola")

        o.add(o1,o2,)




        bot.send_message(call.message.chat.id,"Ichimlik tanlang",reply_markup=o)

    elif call.data == "pepsi":
        o = InlineKeyboardMarkup(row_width=3)
        o1 = InlineKeyboardButton("➖", callback_data="-5")
        o2 = InlineKeyboardButton("0som", callback_data="hisob5")
        o3 = InlineKeyboardButton("➕",callback_data="+5")
        o4=InlineKeyboardButton("🧺Savatga qoshish",callback_data="savat5")
        o.add(o1, o2, o3,o4)
        o4 = open("pepsi.jpg", "rb")
        bot.send_photo(call.message.chat.id,o4,"Pepsi\nNarxi:7000",reply_markup=o)

    elif call.data == "cola":
        o = InlineKeyboardMarkup(row_width=3)
        o1 = InlineKeyboardButton("➖", callback_data="-6")
        o2 = InlineKeyboardButton("0som", callback_data="hisob6")
        o3 = InlineKeyboardButton("➕",callback_data="+6")
        o4=InlineKeyboardButton("🧺Savatga qoshish",callback_data="savat6")
        o.add(o1, o2, o3,o4)
        o5 = open("cola.jpg", "rb")
        bot.send_photo(call.message.chat.id,o5,"Cola\nNarxi:8000",reply_markup=o)
























bot.infinity_polling()