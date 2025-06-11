import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if str(message.from_user.id) == USER_ID:
        bot.reply_to(message, "ربات فعال است و منتظر سیگنال‌هاست.")
    else:
        bot.reply_to(message, "شما مجاز به استفاده از این ربات نیستید.")

# تابع نمونه برای ارسال سیگنال (شما باید اینجا اندیکاتورها را اضافه کنید)
def send_signal(text):
    bot.send_message(USER_ID, f"📊 سیگنال جدید:
{text}")

bot.infinity_polling()
