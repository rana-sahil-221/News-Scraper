import time

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

content = ''

def fetch_news(url):
    print("Fetching Today's Latest News.....")
    print(time.sleep(3))
    cnt = ''
    cnt += ('<b> LATEST NEWS: </b>\n'+'<br>'+'-'*140+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    #print(soup.prettify)
    for i,tag in enumerate(soup.find_all('h2',attrs={'class':'newsHdng'})):
        cnt += (str(i+1)+')'+tag.text+ "\n"+ '<br>')
    return cnt


cnt = fetch_news('https://www.ndtv.com/latest')
print(cnt)
content += cnt
content += ('<br> ----------------------------------------------------------------<br>')
content += ('<br><br> End of Message')

