#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3

from selenium import webdriver
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from pync import Notifier

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

try:

    driver.get("http://192.168.15.1/index.html")

    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="namoswlistitem4"]').click()

    time.sleep(3)

    device_details = driver.find_element_by_xpath('//*[@id="bodyid"]/table/tbody/tr[2]/td[2]/iframe')

    driver.switch_to.frame(device_details)

    battery_level = driver.find_element_by_xpath('//*[@id="batterylevel"]')
    charging_status = driver.find_element_by_xpath('//*[@id="batterystatus"]')

    print(battery_level.text, charging_status.text)

    if(int(battery_level.text[0:2]) <= 20 and charging_status.text == 'Discharging'):
        Notifier.notify('Please charge your JioFi',
                        title = 'Low Battery',
                        subtitle = f'{battery_level.text} remaining ',
                        sound = 'Ping',
                        appIcon = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Reliance_Jio_Logo_%28October_2015%29.svg/1200px-Reliance_Jio_Logo_%28October_2015%29.svg.png')

except:

    driver.quit()
    exit()

driver.quit()
