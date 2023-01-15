import telebot
import pyshorteners

bot = telebot.TeleBot("5879583968:AAEcefwcNIz_ALskE9OOZs744URsZa2TJ_o")

s = pyshorteners.Shortener()

@bot.message_handler(commands=['short'])
def shorten_url(message):
    url = message.text.split()[1]
    shortened_url = s.tinyurl.short(url)
    bot.reply_to(message, shortened_url)

bot.polling()
