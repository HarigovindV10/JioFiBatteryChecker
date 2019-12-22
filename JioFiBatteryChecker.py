#!/usr/bin/env python3

from selenium import webdriver
import time
import os

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome("/Users/harigovindvalsakumar/Downloads/chromedriver", options = options)
try:
    driver.get("http://192.168.15.1/index.html")

    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="namoswlistitem4"]').click()

    time.sleep(3)

    device_details = driver.find_element_by_xpath('//*[@id="bodyid"]/table/tbody/tr[2]/td[2]/iframe')

    driver.switch_to.frame(device_details)

    battery_level = driver.find_element_by_xpath('//*[@id="batterylevel"]')
    charging_status = driver.find_element_by_xpath('//*[@id="batterystatus"]')

    if(int(battery_level.text[0:2]) <= 20 and charging_status.text == 'Discharging'):
        notify(title    = 'Battery Low',
               subtitle = '',
               message  = 'Please charge your JioFi')
except:
    exit()

driver.quit()
