from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from flask import Flask, render_template
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service("C:\\Program Files\\browsers\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service)


class TestNewFacebook:

  def test_launch_facebook(self):
      driver.get('https://www.facebook.com/')
      wait = WebDriverWait(driver, 5)
      create_account_element = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[1]/div/img')))
      att = create_account_element.get_attribute('src')
      if att == 'https://static.xx.fbcdn.net/rsrc.php/y8/r/dF5SId3UHWd.svg':
       Validationresult = 'Pass'
      else:
       Validationresult = 'Fail'
      element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a')
      element.click()
      print(Validationresult)
      return create_account_element


#run_launch_facebook = TestNewFacebook.test_launch_facebook('self') added login feature