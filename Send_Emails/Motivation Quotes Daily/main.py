from bs4 import BeautifulSoup
from rich.console import Console
import requests
import random
import smtplib

FROM_EMAIL = "khanhha.smil@gmail.com"
PASSWORD = "khanhha14042013"
TO_EMAIL = "dungnguyentuan95@gmail.com"

console = Console()


# # source 1

# url = "https://www.inc.com/jeff-haden/100-best-motivational-quotes-to-inspire-anyone.html"
# page = requests.get(url).text
# doc = BeautifulSoup(page, "html.parser")

# page_text = doc.find(class_="standardText lastItem").ol
# quotes = page_text.contents

# with open("quotes.txt", "a") as data_file:
#     for quote in quotes:
#         quote = quote.string
#         if quote != " " and quote != None:
#             data_file.write(f"{quote}\n")

# # source 2


# # source 3

# url = "https://www.inc.com/lolly-daskal/100-motivational-quotes-that-will-inspire-you-to-succeed.html"
# page = requests.get(url).text
# doc = BeautifulSoup(page, "html.parser")

# page_text = doc.find_all(class_="standardText")
# # quote = random.choice(page_text[3:-3]).text


# with open("quotes.txt", "a") as data_file:
#     for quote in page_text[3:-3]:
#         quote = quote.text
        
#         if quote[2] == " ":
#             quote = quote[3:]
#         elif quote[3] == " ":
#             quote = quote[4:]
#         elif quote[4] == " ":
#             quote = quote[5:]

#         data_file.write(f"{quote}\n")


# Send email
with smtplib.SMTP("smtp.gmail.com") as connection:
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
        random_quote = random.choice(quotes)
        console.log(random_quote)

        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)

        MESSAGE = f"Subject:Motivation Quotes\n\n{random_quote}"
        connection.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
        console.log("Send email successful.", style="bold green")