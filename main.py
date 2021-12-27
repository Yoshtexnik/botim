import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("851600929:AAELSYes5w__9GK0IvotZNH64GZ9Rft9xdA")


main_btn = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('Konspekt Yozish ✍', callback_data='kanspekt')
    ]]
    )
dashdurchi = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('dashturchi',url='http://t.me/niyatjon20_01')
    ]]
    )
    
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "Salom", reply_markup=main_btn)

@bot.callback_query_handler(func=lambda call: True)
def calls(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    if call.data == 'kanspekt'
        msg=bot.edit_message_text("📃 Konspekt yozish uchun menga text yuboring",chat_id,msg_id,reply_markup=dashdurchi)
        bot.register_next_step_handler(msg, kanspek)
   
def kanspek(msg):
    txt = msg.text
    rasm = f"https://apis.xditya.me/write?text={txt}"
    bot.send_photo(msg.chat.id, rasm, caption=f"Rasm tayyor\n\nSiz yuborgan soʻz: {txt}")


bot.polling()
