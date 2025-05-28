from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept-Language": "en-US,en;q=0.5"
}
url = "https://www.amazon.com/Lenovo-Legion-i7-14650HX-2560x1600-G-Force/dp/B0DG96DS37/ref=sr_1_10?dib=eyJ2IjoiMSJ9.JHufVZF-RQcfXoAhYzmiD0h0ffR1KQaqcdQ0OtV98mM3cm5wDvZzklWu9KNC9t2weVyOshxhCfMhnbVtlYbh2Lv8J4QfdmlhtffJxKM0EztiCGslIuN85MSFyBc4oPTr8e0WsrgbsiRsKc_K2KEEoHSTEPJLbVygztd96YGoa6x7W2b4ea_zb34Z2LztUwtGD0mouP6q7F71U119tQV1L4zwnCQllDjg9KdqiLWPgP8.3tTePEzmuMLSUn3h33g4agT03QZdONR0w-Ne_NTAY5Q&dib_tag=se&keywords=lenovo+legion&qid=1748433096&sr=8-10"
response = requests.get(url, headers=header)
website_html = response.content
soup = BeautifulSoup(website_html,"html.parser")
price = soup.find(name="span",class_="aok-offscreen").get_text()
# fraction = float(soup.find(name="span",class_="a-price-fraction"))
# print (price.text +fraction.text)
cost = price.split("$")[1]
float_cost = float(cost.replace(",", ""))
print(float_cost)


title = soup.find(id="productTitle").get_text().strip()


# Set the price below which you would like to get a notification
BUY_PRICE = 1900
message = f"{title} is being sold for {float_cost}"
if float_cost < BUY_PRICE:
      with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )