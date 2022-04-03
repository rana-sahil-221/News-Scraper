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
    cnt += ('<b> LATEST NEWS NDTV </b>\n'+'<br>'+'-'*140+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    #print(soup.prettify)
    for i,tag in enumerate(soup.find_all('h2',attrs={'class':'newsHdng'})):
        cnt += (str(i+1)+') '+tag.text+ "\n"+ '<br><br>')
    return cnt


cnt = fetch_news('https://www.ndtv.com/latest')
#print(cnt)
content += cnt
content += ('<b>'+'-'*140+'<b>')
content += ('<br><br> End of Email')

SERVER = 'smtp.gmail.com'
PORT = 587 #gmail default port number
FROM = 'ENTER_YOUR_EMAIL'
TO = 'RECIEVER_EMAIL'
PASS = '***********'

msg = MIMEMultipart() #empty object for message body
msg['Subject'] = 'Latest News Headlines From NDTV [AUTOMATED Email]'+' '+str(now.day)+ '-' +str(now.month)+ '-' +str(now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content,'html')) #converting into html format
#print(msg)

print(time.sleep(2))
print('Initializing Mail Server')

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(0) #1 for debug message
server.ehlo
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())
print("Mail sent Successfully!!")

server.quit()


