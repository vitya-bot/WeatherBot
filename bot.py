import pyowm
import telebot
from telebot import apihelper

apihelper.proxy = {'https':'http://157.245.224.29:80'}

bot = telebot.TeleBot("1130432718:AAFnj5HeC8iDUr0e60iYtpeAu6E2vP-Kx1Y")
owm = pyowm.OWM("5224eaf4f7b2ba8cf6b9156b7ebc7aff", language ="ru")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    
    answer = "в городе  " + message.text + " сейчас " + w.get_detailed_status() +"\n"
    answer += "Температура в районе " + str(temp) + "\n\n"
    
    if temp < 10:
        answer += "Одевайся потеплее, ну =)"
    elif temp < 20:
        answer += "Окей, холодновато, шапку надо надеть)"
    else:
        answer += "В этот город ты никогда не попадёшь, смирись)"
    
    bot.send_message(message.chat.id, answer )
    
bot.polling( none_stop = True,)