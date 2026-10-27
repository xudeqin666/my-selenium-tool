from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.action_chains import ActionChains
from json import load
#import pickle
from time import sleep
dataresult2=[]
dataresult=[]
#import re
import re
from os import system
#import os
idcode=input("idcode:")
n=int(input("number:"))
filename=input("jsonname:")
with open(filename,"r") as file:
    dataresult2=load(file)
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
browser = webdriver.Chrome(chrome_options=options)
#browser = webdriver.Chrome()
browser.maximize_window()

#filename="8.json"

##filename="numbers3duo.json"
##with open(filename,"r") as file:
##    dataresult=json.load(file)
    #print(dataresult2)
url=input("url:")  
browser.get(url)
#browser.get("https://10.112.115.154")

browser.find_element_by_xpath('//input[@tabindex="0"]').send_keys(idcode)#" 输入手机号或姓名
sleep(2)
browser.find_element_by_xpath('//input[@type="password"]').send_keys("Yzcwd+123")
sleep(6)


browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[4]/input').click()#点击登录
#browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div[3]/div/div/div/div[3]/table/tbody/tr[1]/td[9]/a').click()
sleep(6)
#browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span').click()#考试下拉菜单   
#browser.find_element_by_xpath('html/body/div[6]/div/div/div[1]/div[3]/div/div/div/div[3]/table/tbody/tr/td[6]/a').click()#管理员
sleep(3)

#browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li/span').click()  #下菜单中的考试
sleep(15)# 手工点击参加考试
#browser.find_element_by_xpath('//button/span[contains(text(),"参加考试")]').click()  #参加考试

sleep(3)
#browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div[2]/section/div/section/main/div[3]/div[1]/button/span').click() #点击开始考试
##WebDriverWait(browser,20).until(EC.alert_is_present())
##alert.accept()#对弹出的对话框确认
sleep(6)

i=1
#n+1
k=1
for i in range(1,n+1):#

    qusetion_1_title=browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div/section/div/section/main/div/div[1]/form/div[2]/div/span').text #获取题目
    title=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?“”;！，≤ ≥＜《》：。:？、；~@#￥%……&*（）]+", "",qusetion_1_title)
    title=re.sub(r'\-----.*','',title)
    qusetion_1_modle=browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div/section/div/section/main/div/div[1]/form/div[1]/div/span').text #获取题目类型
    modle=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?“”;！，≤ ≥＜《》：。:？、；~@#￥%……&*（）]+", "",qusetion_1_modle)
    modle=re.sub(r'\-----.*','',modle)
    selcet_next = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/section/div/section/main/div/div[1]/div[1]/div[3]/button/span")#点击下一题    selcet_next = browser.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div[2]/section/div/section/main/div/div[1]/div[1]/div[3]/button/span")#点击下一题
    #print(title)
    #if i < 41:
    selcet_1 = browser.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div/section/div/section/main/div/div[1]/form/div[3]/div[1]/div/label/span[2]/span")
    selcet_2 = browser.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div/section/div/section/main/div/div[1]/form/div[3]/div[2]/div/label/span[2]/span")
    try:
        selcet_3 = browser.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div/section/div/section/main/div/div[1]/form/div[3]/div[3]/div/label/span[2]/span")
    except:
        pass
    try:
        selcet_4 = browser.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div/section/div/section/main/div/div[1]/form/div[3]/div[4]/div/label/span[2]/span")
    except:
        pass
    try:
        selcet_5 = browser.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div/section/div/section/main/div/div[1]/form/div[3]/div[5]/div/label/span[2]/span")
    except:
        pass
    for t in range(0,len(dataresult2)):
        if title == dataresult2[t][0] :
        #if dataresult2[t][0] in title:  
            if "A"in dataresult2[t][1] : selcet_1.click()
            if "对"in dataresult2[t][1] : selcet_1.click()
            if "B"in dataresult2[t][1] : selcet_2.click()
            if "错"in dataresult2[t][1] : selcet_2.click()
            if "C"in dataresult2[t][1] : selcet_3.click()
            if "D"in dataresult2[t][1] : selcet_4.click()
            if "E"in dataresult2[t][1] : selcet_5.click()
    sleep(1)
    if "多选题"in modle: selcet_next.click()  
##    selcet_next = browser.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div[2]/section/div/section/main/div/div[1]/div[1]/div[3]/button/span")#点击下一题
##    selcet_next.click()
    sleep(3)
    i=i+1
            
sleep(300)

#system('taskkill /im geckodriver.exe /F')
