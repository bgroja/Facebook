import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By

import test_facebookc
from test_facebook import TestNewFacebook
from selenium.webdriver.chrome.service import Service
from flask import Flask, render_template
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
app = Flask(__name__)

service = Service("C:\Program Files\browsers\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service)


@app.route('/')
def run_testcases():
    return render_template("facebook.html")


@app.route('/run_testcases', methods=['POST'])
def test_case_results():
    Validationresult = test_Url()
    return render_template("facebook.html", Validationresult=Validationresult)
def test_Url():
    driver.get("https://www.facebook.com")
    element = TestNewFacebook.test_launch_facebook('self')
    element.click()
    Validationresult = 'Passed'
    return Validationresult


def launch_webaddress():
    webbrowser.open('http://127.0.0.1:5001/')


if __name__ == '__main__':
    app.run(port=5001)
    launch_webaddress()











