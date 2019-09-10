import os
from flask import Flask, render_template, request,send_from_directory
from uuid import uuid4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pymongo
from pymongo import MongoClient, DESCENDING
class userexception(Exception):
    def __init__(self,message):
              self.message=message
client = pymongo.MongoClient("mongodb://ocr:ocr123@cluster0-shard-00-00-vyttn.mongodb.net:27017,cluster0-shard-00-01-vyttn.mongodb.net:27017,cluster0-shard-00-02-vyttn.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
if (client):
    print("connected")
db = client.text
collection = db.folder2
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
options.add_argument('headless')
__author__ = 'ibininja'

app = Flask(__name__,template_folder='template')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")
@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
        driver = webdriver.Chrome(options=options, executable_path=r"C:\drivers\chromedriver.exe")
        driver.get("https://www.newocr.com/")
        time.sleep(1)
        k=destination.split('//')
        path=destination
        print(path)
        try:
            box = driver.find_element_by_xpath("//input[@id='userfile']").send_keys(path)
            btn = driver.find_element_by_xpath("//button[@id='preview']").click()
            time.sleep(1)
            btn2 = driver.find_element_by_xpath("//button[@id='ocr']").click()
            time.sleep(2)
            txt = driver.find_element_by_xpath("//textarea[@id='ocr-result']").text
            lis = txt.split('TC_')
            lis = ['TC_' + i for i in lis]
           # lis=[i.replace(' ','|') for i in lis]
            str1 = '----\n'.join(map(str, lis))
            print('\n'.join(map(str, lis)))
            str1.replace('TC_----','')
            #return send_from_directory("images", )
            return render_template('display.html', path=k[1], result=str1,file=filename)
        finally:
            driver.quit()

@app.route('/show/<filename>')
def show(filename):
    return send_from_directory("images", filename)
@app.route('/csv')
def csv():
    import pymongo
    import pandas as pd
    from pymongo import MongoClient, DESCENDING
    client = pymongo.MongoClient(
        "mongodb://ocr:ocr123@cluster0-shard-00-00-vyttn.mongodb.net:27017,cluster0-shard-00-01-vyttn.mongodb.net:27017,cluster0-shard-00-02-vyttn.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    if (client):
        print("connected")
    db = client.text
    collection = db.folder4
    doc = collection.find({})
    for i in doc:
        print(i['sid'])
    test = pd.DataFrame(list(collection.find({})))
    print(test)
    export_csv = test.to_csv(r'D:\folder4.csv', index=None, header=True)
    return 'file saved to C:/Users\Manoj\Desktop\export_dataframe.csv'
@app.route('/process',methods=['POST','GET'])
def process():
    txt=request.form['subject']
    imageno=request.form['imageno']
    print(txt)
    lis=txt.split('----')
    #lis.pop('TC_----')
    no=1
    for i in lis:
        print(i)
        print('-----------------------------------------------------')
        k=i.split('|')
        print(len(k))
        k=[i.replace('\r\n','') for i in k]
        try:
            if len(k)!=19:
                raise userexception('fields are below 19')
        except userexception as e:
            print(e.message)
            return render_template('complete.html',field=k[0],totalform=k,l=len(k))
        id=k[0]
        id=id.replace('\r\n','')
        sid=id
        date=k[1]
        phone_number=k[2]
        load=k[3]
        modelnumber=k[4]
        contract=k[5]
        contract=contract.title()
        s1=k[6]
        s2=k[7]
        s3=k[8]
        rental=k[9]
        rental=rental.title()
        work=k[10]
        work=work.title()
        email=k[11]
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
        address=k[12]
        print(address.replace('\n', ' ').replace('\r', ''))
        address=man(address.replace('\n', ' ').replace('\r', ''))
        print('+++++++++++++++++++++++++++++++++++')
        print(address)
        s4=k[13]
        s5=k[14]
        cardtype=k[15]
        cardtype=cardtype.title()
        cardno=k[16]
        secdate=k[17]
        quality=k[18]
        doc=collection.find({'sid':sid}).count()
        print(doc)
        # try:
        if doc==0:
                    collection.insert_one({'id':'','sid':sid,'date':date,'phone_number':phone_number,'load':load,'modelnumber': modelnumber,'contract':contract,'s1':s1,'s2':s2,'s3':s3,
                    "rental":rental,'work':work,'email':email,'address':address,'s4':s4,'s5':s5,'cardtype':cardtype,'cardno':cardno,'secdate': secdate,
                    'quality':quality,'image_name':imageno,'form_no':no})
        # except:
        #     collection.insert_one({'id': '', 'sid': sid, 'date': date, 'phone_number': phone_number, 'load': load,
        #                            'modelnumber': modelnumber, 'contract': contract, 's1': s1, 's2': s2, 's3': s3,
        #                            "rental": rental, 'work': work, 'email': email, 'address': address, 's4': s4,
        #                            's5': s5, 'cardtype': cardtype, 'cardno': cardno, 'secdate': secdate,
        #                            'quality': quality})
        print(k)
        no=no+1
    doc=collection.find({})
    return render_template('result.html',doc=doc)
if __name__ == "__main__":
    app.run(port=4555, debug=True)