"""
Day 24-25 - web scraper and email sender automation
Author - Uma
Date - 2-11-2026
"""

import requests
import smtplib
import os

from bs4 import BeautifulSoup
from email.message import EmailMessage

# 1. scrape website
url = "https://quotes.toscrape.com/"

response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

# 2. extract quotes and authors
content = "today's quotes \n\n"

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    content += f"quote : {text} \n"
    content += f"author : {author} \n"
    content += "-"*40 + "\n"

# 3. display scraped information
print(content)

# 4. prepare email
sender = os.environ["EMAIL_ADDRESS"]
password = os.environ["EMAIL_APP_PASSWORD"]
receiver = os.environ["TO_EMAIL"]

msg = EmailMessage()

msg["subject"] = "daily quotes - python automation"
msg["from"] = sender
msg["to"] = receiver

msg.set_content(content)

# 5. send email
with smtplib.SMTP_SSL("smtp.gamil.com",465) as server:
    server.login(sender, password)
    server.send_message(msg)

print("email sent successfully!")