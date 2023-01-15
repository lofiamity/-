5879583968:AAEcefwcNIz_ALskE9OOZs744URsZa2TJ_o
    
import pyshorteners
import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")
s = pyshorteners.Shortener()

@bot.message_handler(commands=['short'])
def shorten_url(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, "Invalid command. Please include a URL to shorten after the '/short' command.")
    else:
        url = message.text.split()[1]
        shortened_url = s.tinyurl.short(url)
        bot.reply_to(message, shortened_url)

@bot.message_handler(func=lambda message: not message.text.startswith('/'))
def send_help(message):
    bot.reply_to(message, "Please use /short command followed by URL you want to shorten")

bot.polling()
