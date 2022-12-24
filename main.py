from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys # özel karakterler için kütüphane
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://www.kodlama.io/")
driver.maximize_window() # ekranı tam boyuta getirir.

WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(By.XPATH,"//*[@id='navbar']/div/div/div/ul/li[3]/a")) #defansif kodlama

loginBtn = driver.find_element(By.XPATH,"//*[@id='navbar']/div/div/div/ul/li[3]/a")
# loginBtn texti "Giriş Yap" olmalıdır.
loginBtnText = loginBtn.text

#windows + .
if loginBtnText == "Giriş Yap":
    print("Test başarılı 😎")
else:
    print("Test Başarısız ❌")

# ekran görüntüsü alma
# kaydetme
# element bazlı, ya da driver bazlı alınabilir.
loginBtn.screenshot("element.png") # =>  elementin ss'ini alır
driver.save_screenshot("screen.png") # =>  tüm ekranın ss'ini alır

# scroll_to fonksiyonu => locate edilmiş bir element'e scroll yapar.
# element.scroll_to
# slenium son sürümlerinden kaldırıldı.
# javascript kullanılarak scroll edilecek...
terms_conditions = driver.find_element(By.XPATH,'/html/body/div[1]/footer/div/div/div[2]/ul/li[1]/a')
sleep(2)
# driver.execute_script("window.scroll(0,900)")  #--- yöntem 1.
# driver.execute_script("arguments[0].scrollIntoView()",terms_conditions)  #--- yöntem 2.


# ActionChains => Yapılacak aksiyonları sırala ve perfom dediğimde bu işlemler sırası ile gerçekleştirilsin.

# elemana scroll ol => ss al => butona tıkla
# perform
actions = ActionChains(driver)
actions.move_to_element(terms_conditions)
actions.click(terms_conditions)
actions.perform() # zincirlenen aksiyonları işleme koyar.

# PG_DWN scroll yapmak için, amatörce çok kullanılmaz
# özel karakterler nasıl kullanılır => Caps, Shift, Ctrl, Alt, PG_DWN, PG_UP, Insert

# actions.send_keys(Keys.PAGE_DOWN)

# 2 adet test case verilecek
# bu test caseler otomatize edilecek
# sonuçlar konsola yazdırılacak
# ekran görüntüsü günün tarihi ile kaydedilecek -> date.today() -> driver.save_screenshot(str(date.today()) + '(1).png') ve driver.save_screenshot(str(date.today()) + '(2).png')

# WebDriverWait classı => sitenin ya da elementin yüklenmesi beklenmesi için kullanılan kütüphane
# condition bazlı çalışır
# loginBtn görünür olana kadar max 5 sn bekle.

# pytest => 
# pytest dosyaları "test_" prefixi (ön ek) ile başlar. Örnek = test_Kodlamaio gibi
# pytest classları "Test_" prefixi ile başlar.
# pytest fonksiyonları "test_" prefixi ile başlar.

# constants


input()
