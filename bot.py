import telebot
import requests
import os
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

def download_insta(link):
    api = f"https://api.oust.me/instagram?url={link}"
    r = requests.get(api).json()
    return r["url"]

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Salom 👋\nMengaga Instagram video link yuboring 📥")

@bot.message_handler(func=lambda message: True)
def insta_down(message):
    try:
        url = download_insta(message.text)
        bot.send_video(message.chat.id, url, caption="🎬 Yuklab olindi!")
    except:
        bot.reply_to(message, "❌ Xato link! Yana urinib ko‘ring.")

bot.polling()
