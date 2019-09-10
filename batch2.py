import pymongo
import pandas as pd
from pymongo import MongoClient, DESCENDING
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient, DESCENDING
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
client = pymongo.MongoClient("mongodb://localhost:27017/")
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
if (client):
    print("connected")
db = client.localtext
collection = db.folder4
doc=collection.find({},no_cursor_timeout=True).skip(200).limit(200)
for i in doc:
    print(i['_id'])
    img=i['image_name']
    form=i['form_no']
    def man(s):
        s = s.title()
        s = s.split(' ')
        l = 0
        for i in s:
            i = str(i)
            if i.isalpha() == True:
                pass
            else:
                s[l] = i.upper()
            if len(i) == 2:
                s[l] = i.upper()
            l = l + 1
        print(' '.join(s))
        return (' '.join(s))
    print(i['address'])
    newaddress=man(i['address'])
    print(newaddress)
    print(i['email'])
    email=i['email'].lower()
    print(email)
    imglis=img.split('_')
    print(imglis)
    if len(str(form))==1:
            imgno=str(imglis[0])+'_'+str(imglis[1])+'000'+str(form)
            print(imgno)
    else :
        imgno = str(imglis[0]) + '_' + str(imglis[1]) +"00"+ str(form)
        print(imgno)
    print(imgno)
    dte=i['date']
    print(dte)
    driver.find_element_by_xpath('//input[@id="text-datetime"]').send_keys(Keys.CONTROL + "a")
    driver.find_element_by_xpath('//input[@id="text-datetime"]').send_keys(Keys.DELETE)
    time.sleep(1)
    driver.find_element_by_xpath('//input[@id="text-datetime"]').send_keys(dte)
    driver.find_element_by_xpath('//input[@id="text-format"]').send_keys(Keys.CONTROL + "a")
    driver.find_element_by_xpath('//input[@id="text-format"]').send_keys(Keys.DELETE)
    driver.find_element_by_xpath('//input[@id="text-format"]').send_keys('%B %d,%Y')
    time.sleep(1)
    datetext=driver.find_element_by_xpath('//div[@id="text-result"]').text
    print(datetext)
    secdte=i['secdate']
    print(secdte)
    driver.find_element_by_xpath('//input[@id="text-datetime"]').send_keys(Keys.CONTROL + "a")
    driver.find_element_by_xpath('//input[@id="text-datetime"]').send_keys(Keys.DELETE)
    time.sleep(1)
    driver.find_element_by_xpath('//input[@id="text-datetime"]').send_keys(secdte)
    driver.find_element_by_xpath('//input[@id="text-format"]').send_keys(Keys.CONTROL + "a")
    driver.find_element_by_xpath('//input[@id="text-format"]').send_keys(Keys.DELETE)
    driver.find_element_by_xpath('//input[@id="text-format"]').send_keys('%B %d,%Y')
    time.sleep(1)
    datetext2= driver.find_element_by_xpath('//div[@id="text-result"]').text
    print(datetext2)
    consstring = 'TC_vd - Sdi - IB - BtunVp-'
    sidsplit = i['sid'].split('-')
    le = len(sidsplit)
    sidno = sidsplit[le - 1]
    newsid = consstring + str(sidno)
    print(newsid)
    model=''
    if  '-' in i['modelnumber'] :
           modelsplit=i['modelnumber'].split('-')
           nextmodel=modelsplit[1:]
           print(nextmodel)
           n=''
           for k in nextmodel:
               n=n+'-'+k
           print(n)
           print(n)
           model = modelsplit[0].title()+n
           #model=modelsplit[0].title()+''+join(map(str, lnextmodel))
           print(model)
    else:
        model=i['modelnumber'].title()
        print(model)
    print(model)
    collection.update_one({'_id':i['_id']},{'$set':{
        'id':imgno,
        'sid':newsid,
        'modelnumber':model,
        'date':datetext,'email': i['email'].lower(),
        'secdate':datetext2,'address':newaddress,'status':1
    }
    })

#export_csv = test.to_csv (r'C:\Users\Manoj\Desktop\export_dataframe.csv', index = None, header=True)
