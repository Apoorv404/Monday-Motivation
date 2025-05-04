import smtplib
import datetime as dt
from random import choice

my_email = ""
password = ""
recipant_email = ""
current_day = dt.datetime.now().weekday()

with open("quotes.txt") as file:
    quote_list = file.readlines()

if current_day == 1:
    random_quote = choice(quote_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipant_email,
                            msg=f"Subject:Monday Motivation\n\n{random_quote}")
