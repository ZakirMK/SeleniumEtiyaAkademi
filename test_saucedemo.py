from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.common.keys import Keys
from constants import *

class Test_Saucedemo:
    

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_DOMAIN_URL)  


    def teardown_method(self):
        self.driver.quit()
        
    # -Doğru bilgilerden standard_user kullanıcı adıyla giriş yapılmanın doğru olup olmadığı kontrol edilmelidir.
    def test_login_standart_user(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
        userName= self.driver.find_element(By.ID, USERNAME_ID )
        userName.send_keys(USERNAME)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
        passwordID= self.driver.find_element(By.ID, PASSWORD_ID )
        passwordID.send_keys(PASSWORD)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
        loginID= self.driver.find_element(By.ID,LOGIN_ID)
        loginID.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USER_MENU )))
        userMenu= self.driver.find_element(By.ID,USER_MENU)

        userMenuText=userMenu.text

        assert userMenuText == MENU_TEXT

    # -Yanlış bilgiler girildiğinde uyarı çıkıp çıkmadığı test edilmelidir.
    def test_login_undefined(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
        userName= self.driver.find_element(By.ID, USERNAME_ID )
        userName.send_keys(USERNAME)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
        passwordID= self.driver.find_element(By.ID, PASSWORD_ID )
        passwordID.send_keys(WRONG_PASSWORD)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
        loginID= self.driver.find_element(By.ID,LOGIN_ID)
        loginID.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, ERROR_LOGIN )))
        errorMenu= self.driver.find_elements(By.XPATH,ERROR_LOGIN)
        errorMenuSize = len(errorMenu)

        assert errorMenuSize > 0 
        
    # -Yanlış bilgiler girildiğinde çıkan uyarı mesajının doğruluğu kontrol edilmelidir Epic sadface: Username and password do not match any user in this service   
    def test_login_error_message(self):
        self.test_login_undefined()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, ERROR_LOGIN)))
        errorMenu= self.driver.find_element(By.XPATH,ERROR_LOGIN)
        errorMenuText = errorMenu.text

        assert errorMenuText == ERROR_MENU_TEXT
        
    # -Ana sayfada 6 adet ürün listelendiği kontrol edilmelidir.
    def test_inventory_list(self):
        # Başarılı login fonksiyonunu çağırma
        self.test_login_standart_user()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, INVENTORY_LIST)))
        inventory = self.driver.find_elements(By.XPATH, INVENTORY_LIST)
        inventorySize = len(inventory)

        assert inventorySize == 6

    # -Sepete Ekle butonuna tıklandığında butonun texti REMOVE olmalıdır.
    def test_basket(self):
        # Başarılı login fonksiyonunu çağırma
        self.test_login_standart_user()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, PRODUCT1_ID)))
        product1 = self.driver.find_element(By.ID, PRODUCT1_ID)
        product1.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME, PRODUCT_REMOVE_NAME)))
        productRemove = self.driver.find_element(By.NAME, PRODUCT_REMOVE_NAME)
        productRemoveText = productRemove.text

        assert productRemoveText == PRODUCT_REMOVE_TEXT
        
    # -Sepete 1 adet ürün eklendiğinde sağ üstteki sepet üzerinden 1 sayısı çıkmalıdır.
    def test_basket_item_number(self):
        self.test_login_standart_user()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, PRODUCT1_ID)))
        product1 = self.driver.find_element(By.ID, PRODUCT1_ID)
        product1.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, BASKET_ITEMS)))
        basket_items = self.driver.find_element(By.CLASS_NAME, BASKET_ITEMS)
        basket_itemsText = basket_items.text

        assert basket_itemsText == BASKET_ITEMS_COUNT
