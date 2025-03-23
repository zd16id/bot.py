import google.generativeai as genai
import telebot
from telebot import *
# قم بتخزين التوكن ومفتاح API في متغيرات البيئة بدلاً من وضعها في الكود مباشرةً
token = "7776694559:AAEi_89cMqPvFdqE3tqFN16itTN6fKjnRKU"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "مرحبًا بك في بوت الذكاء الاصطناعي! 🌟 \n تم تطوير هذا البوت بواسطه الطالب زيد  لمساعدتك في تعلم الحاسوب بشكل ممتع واحترافي وفهم :لغه سكراتش وسناب. والمصفوفات والاوفيس. بطريقه سهله وفعاله 🚀 \n لوزارة تربيه الكرخ الثانيه مدرسة اللطيفيه للبنين")

@bot.message_handler(func=lambda message: True)

def echo(message):
    text=message.text
    send=ask(text)
    bot.send_message(message.chat.id, send)



def ask(m):
   genai.configure(api_key="AIzaSyCW0ccPaVxp8IC-qD4gy6U7V8MVZBfGzKk")
   model = genai.GenerativeModel("gemini-1.5-flash")
   response = model.generate_content(m)
   return response.text
bot.polling()
