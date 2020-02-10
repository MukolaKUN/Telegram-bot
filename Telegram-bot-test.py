import telebot


token = '985777845:AAGgJj1YSYONQIJsKUNVYAbv19u1vnqjdF4'
bot = telebot.TeleBot(token)


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])

def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

@bot.message_handler(content_types=['sticker'])

def send_stiker(message):
    print(message)
    if message.text.lower() == 'жопа':
        bot.send_sticker(message.chat.id, 'AgADCgADwDZPEw')
    else:
        bot.send_message(message.chat.id, 'I love You too')




bot.polling()

