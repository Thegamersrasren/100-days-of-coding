from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


website = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(website)
firstname = driver.find_element(By.NAME,value="fName")
firstname.send_keys("garen")
lastname = driver.find_element(By.NAME,value="lName")
lastname.send_keys("agbaire")
email = driver.find_element(By.NAME,value="email")
email.send_keys("garenagabire@gmail.com")
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")

button.click()