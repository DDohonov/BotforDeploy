import telebot
import random
import os 


bot=telebot.TeleBot('5712136718:AAFw57oSZdrj8ptT2ytxmm3O5O38gCrOlh4')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,'Добрий день Джавелін')
    

@bot.message_handler(content_types=['sticker'])
def stickers(message):
    bot.reply_to(message,'Мені байдуже на твоії емоції')

@bot.message_handler(content_types=['text'])
def mem(message):
    with open("D:\\Задания\\W\\1.jpg",'r') as f:
     bot.send_photo(message.chat.id,f)
    
bot.infinity_polling()

