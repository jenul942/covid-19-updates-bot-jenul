import telebot
import requests
from bs4 import BeautifulSoup

api = '1567686966:AAEiSjfU9GKXXrSnpgQvHmXoW-c8iOz-HOE'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=["help", "hlp", "feedback"])
def hello(message):
    bot.send_message(message.chat.id, "Any feedback @JenulRanthisa")

@bot.message_handler(commands=['details'])
def details(message):
  page = requests.get('https://www.worldometers.info/coronavirus/country/sri-lanka/')
  after_bs = BeautifulSoup(page.content, 'html.parser')
  find_data = after_bs.find_all(id="maincounter-wrap")
  output = ''
  for x in find_data:
  	  # print(x.text)
  	  output = output + x.text
  
  bot.reply_to(message, output)

print('bot is running.....')

bot.polling()