from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
URL = "https://appbrewery.github.io/Zillow-Clone/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(URL, headers=headers)
website_html = response.text
soup = BeautifulSoup(response.text, 'html.parser')
price_elements = soup.find_all('span', {'data-test': 'property-card-price', 'class': 'PropertyCardWrapper__StyledPriceLine'})
links_elements = soup.find_all('a',{'data-test':'property-card-link','class':'property-card-link'})
address_elements = soup.find_all('address',{'data-test':'property-card-addr'})
#price list
clean_prices = [
    price.get_text(strip=True)
    .replace("$", "")
    .replace("+", "")
    .replace("/mo", "")
    .replace("1 bd", "")
    .replace("1bd", "")
    .replace(",", "")
    .strip()
    for price in price_elements
]
#link list
link_list = [link.get('href') for link in links_elements]
#address list
address_list = [address.get_text(strip = True) for address in address_elements ]



for n in range(len(link_list)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfZGRb6AltCQTA42OmuWulfNBx9BS5umZtZs7dcdxmcc1gv-w/viewform?usp=header")
    time.sleep(2)
    address = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    address.send_keys(address_list[n])
    price.send_keys(clean_prices[n])
    link.send_keys(link_list[n])
    submit_button.click() 