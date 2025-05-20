#tested with an actual password and mail if using this code replace the emails in the main.py 
#and the one in the birthday file


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "ctqgumhuaiwtosjm"

today = datetime.now()
today_ = (today.month, today.day)

data = pandas.read_csv("birthday.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_ in birthdays_dict:
    birthday_person = birthdays_dict[today_]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
