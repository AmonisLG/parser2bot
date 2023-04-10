import telebot
import requests
import time

from bs4 import BeautifulSoup

token ="6231221204:AAGJ2wHHVrqGpBrGX-HmCM2Gw7mYoV2ZwJc"
id_channel = "http://t.me/Amnor34bot"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def commands(message):
    if message.text == "start":
        back_post_id = 0
        while True:
            post_text = (back_post_id)
            back_post_id = post_text[1]

            if post_text[0] != None:
                bot.send_message(id_channel, post_text[0])
                time.sleep(4)

def parser(back_post_id):
    URL = 'https://habr.com/ru/search/?q=python&target_type=posts&order=relevance'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find("h2", class_="tm-title__link")
    post_id = post["id"]

    if post_id !=back_post_id:
        title = post.find("a", class_="tm-title tm-title_h2").text.strip()
        description = post.find("div", class_="tm-article-body tm-article-snippet").text.strip()
        url = post.find("a", class_="tm-title tm-title_h2", href=True)["href"].strip

        return f"{title}\n\n{description}\n\n{url}"
    else:
        return None, post_id

bot.polling()