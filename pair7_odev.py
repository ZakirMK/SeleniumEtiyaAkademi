from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.kodlama.io/")

# ekranı tam boyutuna getirir
driver.maximize_window() 
kurs = driver.find_elements(By.XPATH,'//*[@class="course-box-image-container"]') 
# Toplam kursları sayar.
kursSayisi = len(kurs)
#checkTitleText = checkTitle.text
if kursSayisi == 6:
    print("Kurs sayısı testi başarılı!😎", " Toplam Kurs adeti:" + str(kursSayisi))
else:
    print("Kurs sayısı testi başarısız!❌")
driver.save_screenshot(str(date.today()) + '(1).png')

sleep(2)

search = driver.find_element(By.ID,"search-courses")
# arama ekranında istenilen kelimeleri aratır
search.send_keys("senior")
sleep(2)
# Başlığın Senior Yazılım Geliştirici Yetiştirme Kampı (.NET) olup olmadığını sorgular.
title = driver.find_element(By.XPATH,'//*[@title="Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)"]')
titleTest = title.text
sleep(2)
if titleTest == "Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)":
    print("Arama testi başarılı!😎")
else:
    print("Arama testi başarısız!❌")
driver.save_screenshot(str(date.today()) + '(2).png')
input()