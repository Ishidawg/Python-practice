from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

browser = webdriver.Chrome()

print("Starting type messages...")

for i in range(10):
    browser.find_element(By.XPATH,'//*[@id="channels"]/ul/li[2]').click()
    browser.find_element(By.XPATH,'//*[@id="app-mount"]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]').send_keys('hello')
    pyautogui.press('enter')