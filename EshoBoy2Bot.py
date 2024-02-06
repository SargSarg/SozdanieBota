import telebot

TOKEN = "6616575619:AAGKCbatht1aApX6_A7m8z7U3voI68lu-RY"

bot = telebot.TeleBot(TOKEN)

bot.polling(none_stop=True) #polling - метод чтоб запустить бота
#none_stop=True чтоб при возникновении ошибок бот не прекращал работу



#Объявим обработчик сообщений
import telebot

TOKEN = "6616575619:AAGKCbatht1aApX6_A7m8z7U3voI68lu-RY"

bot = telebot.TeleBot(TOKEN)

#@bot.message_handler(filters) #есть разные фильтры
def function_name(message): #название фукнции сами выбираем, аргумент message
    bot.reply_to(message, "This is a message handler")
##################


#теперь объявим обработчик с определенными фильтрами
import telebot

TOKEN = "6616575619:AAGKCbatht1aApX6_A7m8z7U3voI68lu-RY"

bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help']) #фильтр commands для сообщений начинающихся с команд
def handle_start_help(message):
    pass

# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio']) #фильтр content_type для сообщений
def handle_docs_audio(message):
    pass

bot.polling(none_stop=True)


#Сделаем так чтобы обработчик брал из сообщения username и выдавал приветствие пользователю
import telebot

bot = telebot.TeleBot("6616575619:AAGKCbatht1aApX6_A7m8z7U3voI68lu-RY")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, / c{message.chat.username}")


#Либо вот так
import telebot

bot = telebot.TeleBot("6616575619:AAGKCbatht1aApX6_A7m8z7U3voI68lu-RY")
@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message,f"Welcome, {message.chat.username}")

bot.polling(none_stop=True)

#Обработчик который на сообщения с картинками(мемами) будет отвечать nice meme
import telebot

bot = telebot.TeleBot('6616575619:AAGKCbatht1aApX6_A7m8z7U3voI68lu-RY')

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

bot.polling(none_stop=True)