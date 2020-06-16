from plyer import notification
import requests
from bs4 import BeautifulSoup
from time import sleep

def notify_Me(title,message):
    notification.notify(title=title,
                        message=message,
                        app_icon="C:\\Users\\DELL\\Downloads\\corona(1).ico",
                        timeout=5)

def getdata(url):
    r=requests.get(url)
    return r.text

if __name__ == '__main__':
    
    while True:
        my_html_data = getdata('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(my_html_data, 'html.parser')
        # print(soup.prettify())

        mydatastr = ''
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            mydatastr += tr.get_text()

        mydatastr = mydatastr[1:]
        itemlist = mydatastr.split('\n\n')

        states = ['Chandigarh', 'Telangana', 'Uttar Pradesh', 'Delhi', 'Maharashtra', 'Punjab']
        for item in itemlist[0:35]:
            datalist = (item.split('\n'))
            if datalist[1] in states:
                print(datalist)
                ntitle = 'Cases of covid-19'
                ntext = f"{datalist[1]}: Active cases: {datalist[2]}\n Cured/Discharged/Migrated : {datalist[3]}\n deaths : {datalist[4]}\n total Cases : {datalist[5]}\n"
                notify_Me(ntitle, ntext)
                sleep(2)
        sleep(3600) #for every hour
