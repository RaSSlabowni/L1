import telebot

from NumbersToWords import *
import config

bot = telebot.TeleBot(config.Token)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте!")
    bot.send_message(message.chat.id, "Введите число от 1 до 5000.")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Просто введите число от 1 до 5000")


@bot.message_handler(content_types=['text'])
def Convert(message):
    try:
        number = int(message.text)
        if not 1 <= number <= 5000:
            bot.send_message(message.chat.id, "Ваше число не подходит под условия диапазона, введите число заново")
        else:
            msg2usr = (number_to_words(number).capitalize())
            bot.send_message(message.chat.id, deletecharacters(str(msg2usr)))

    except ValueError:
        bot.send_message(message.chat.id, "Не число!")


bot.polling(none_stop=True)
