import pandas as pd
import datetime as dt
import smtplib
import random

my_email = "khanhha.smil@gmail.com"
password = "khanhha14042013"

# Get the current datetime.
now = dt.datetime.now()

# Read birthdays.csv file.
data = pd.read_csv("birthdays.csv")

# Loop through data's row.
for (index, row) in data.iterrows():
    # If today is their birthdays, then send the wisher email.
    if row.day == now.day and row.month == now.month:
        # Pick randomly a letter template and open it.
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as f:
            data = f.read()
            # Replace [NAME] by their names.
            data = data.replace("[NAME]", f"{row['name']}")

            # Send email.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(my_email, password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=f"{row.email}", 
                                    msg=f"Subject:Happy Birthday\n\n{data}")            