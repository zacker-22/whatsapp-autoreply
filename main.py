from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
from random import randint
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot=ChatBot('Zacker')
bot.set_trainer(ListTrainer)

#bot.train("chatterbot.corpus.english")
#Train Chatter bot as per your requirements
binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get('https://wedriver.whatsapp.com')
raw_input('Start? ')

#elem.click()


last=""
lr="None"
count = 0
delay=2
while True:
    
    msg = driver.find_elements_by_class_name('emojitext')
    an=msg[-1].text
    if last!=an and  an != lr and an!="Are You Bored?":
        print last,an
        if an[:6]=='Train:':
            an=an[6:]
            if '-' in an:
                q,a=an.split('-')
                q=q.strip()
                a=a.strip()
                bot.train([q,a])
                reply="Thank You for Teaching me"
            else:
                reply = 'Invalid Format'
            
        else:    
            rep =  bot.get_response(an)
            reply = rep.text
        print reply
        elem1 = driver.find_elements_by_class_name('input')
        elem1[1].send_keys((reply))
        driver.find_element_by_class_name('send-container').click()
        last=an
        count = 0
        lr=str(reply)
    sleep(1)
    count+=1
    if count>10**delay:
        elem1 = driver.find_elements_by_class_name('input')
        elem1[1].send_keys("Are You Bored?")
        driver.find_element_by_class_name('send-container').click()
        count = 0
        delay+=1 
