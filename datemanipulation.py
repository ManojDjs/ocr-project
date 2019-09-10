import time
from selenium import webdriver
import pymongo
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient, DESCENDING
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2,
                                                          'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                          'notifications': 2, 'auto_select_certificate': 2,
                                                          'fullscreen': 2, 'mouselock': 2, 'mixed_script': 2,
                                                          'media_stream': 2,
                                                          'media_stream_mic': 2, 'media_stream_camera': 2,
                                                          'protocol_handlers': 2,
                                                          'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                          'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                          'metro_switch_to_desktop': 2,
                                                          'protected_media_identifier': 2, 'app_banner': 2,
                                                          'site_engagement': 2, 'durable_storage': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r"C:\drivers\chromedriver.exe")
driver.get("https://jeffkayser.com/projects/date-format-string-composer/index.html")
driver.find_element_by_xpath('//input[@id="text-datetime"]').send_keys(Keys.CONTROL + "a")
driver.find_element_by_xpath('//input[@id="text-datetime"]').send_keys(Keys.DELETE)
time.sleep(1)
driver.find_element_by_xpath('//input[@id="text-datetime"]').send_keys('dec-08-94')
driver.find_element_by_xpath('//input[@id="text-format"]').send_keys(Keys.CONTROL + "a")
driver.find_element_by_xpath('//input[@id="text-format"]').send_keys(Keys.DELETE)
driver.find_element_by_xpath('//input[@id="text-format"]').send_keys('%B %d,%Y')
time.sleep(1)
datetext=driver.find_element_by_xpath('//div[@id="text-result"]').text
print(datetext)
driver.quit()