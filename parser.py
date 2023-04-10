import requests
from bs4 import BeautifulSoup

URL = 'https://habr.com/ru/search/?q=python&target_type=posts&order=relevance'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

post = soup.find("h2", class_="tm-title__link")
title = post.find("a", class_="tm-title tm-title_h2").text.strip()
description = post.find("div", class_="tm-article-body tm-article-snippet").text.strip()
url = post.find("a", class_="tm-title tm-title_h2", href=True)["href"].strip
print(title, description, url, sep="\n\")