##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import random
import smtplib
from datetime import datetime

PLACEHOLDER = "[NAME]"

contact_list = pandas.read_csv("./birthdays.csv")
birthdays = {index: (row.month, row.day) for (index, row) in contact_list.iterrows()}
# You can just use index : row to get the whole row.

time_now = datetime.now()
time_md_now = (time_now.month, time_now.day)

for index, birthdays in birthdays.items():
    if time_md_now == birthdays:
        person_info = (contact_list.iloc[index])
        person_email = (person_info.get('email')).strip()
        person_name = (person_info.get("name")).strip()

        # list_of_letters = ["./letter_1.txt", "./letter_2.txt", "./letter_3.txt"]
        # better way
        random_letter = f"./letter_{random.randint(1,3)}.txt"

        with open(random_letter, "r") as letter:
            read_letter = letter.read()
            final_letter = read_letter.replace(PLACEHOLDER, person_name)

        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user="", password="mockpassword")
            connection.sendmail(from_addr="",
                                to_addrs=person_email,
                                msg="Subject: HAPPY BIRTHDAY!\n\n"
                                    f"{final_letter}")
