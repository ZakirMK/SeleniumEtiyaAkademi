from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()

driver.get("https://www.patika.dev/")
driver.maximize_window() #ekranın tam boyut
loginBtn = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/div/div[2]/div/a")
loginBtnText = loginBtn.text
loginBtn.click()

sleep(3)

input= driver.find_element(By.NAME,"emailAddress")
input.send_keys("adiguzelomerrrr@gmail.com")
input= driver.find_element(By.NAME,"password")
input.send_keys("24517113206.Om")

sleep(3)

signInBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[1]/form/button")
signInText = signInBtn.text
signInBtn.click()

sleep(3)

asilBaslik=driver.title
if  asilBaslik=="Dashboard":
    print("Giriş başarılı")
else:
    print("Giriş başarısız!") 
sleep(10) 