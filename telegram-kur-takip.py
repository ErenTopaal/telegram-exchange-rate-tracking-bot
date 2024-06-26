from bs4 import BeautifulSoup
import requests

while True:
 
    url1 = "https://www.google.com/finance/quote/USD-TRY"

    sayfa = requests.get(url1) #request kütüphanesini kullanarak url1 e git demek 

    html_sayfa = BeautifulSoup(sayfa.content,"html.parser")

    dolar = html_sayfa.find(   "div",class_="YMlKec fxKbKc" ).getText() #doları HTML sayfasından direkt olarak çekiyor
    roundedolar = round(float(dolar.replace(",",".")),2) # doları 2 haneye düşürüyor
    dolarmessage = "Dolar = " + str(roundedolar)+ " TL" #Dolar = "" TL yazdırmaya 

    print(dolarmessage)

    ##Telegram bot 
    from datetime import datetime
    import time

    ap="https://api.telegram.org/bot6835580183:AAFZS7ceNN0Y4KzcAggVFxLyaQoZReZDHUo/SendMessage"

    requests.post(url=ap,data={"chat_id":"1451260285","text":dolarmessage}).json()

    time.sleep(5)

    