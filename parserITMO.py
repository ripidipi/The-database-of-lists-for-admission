import bs4
import time
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  
from bs4 import BeautifulSoup
import requests
import json
from base_classes import Direction, Student, University
 
address = 'https://abit.itmo.ru/'
links = []
with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:  
    driver.get(address + "ratings/bachelor/")
    time.sleep(1)  
    soup = BeautifulSoup(driver.page_source, 'html.parser')  
    div_tag = soup.find('div', 'DirectionsList_cards__NWRcz')
    links = div_tag.find_all('a')

direct = []

for i in links:
    name = i.find('p')
    q_place = i.find_all('div')
    d = Direction('ITMO' + str(name)[3:-4].split(' ')[0].replace('.', '_'), str(q_place[1])[5:-6], address + str(i).split()[2][7:34])
    # print(str(name)[3:-4].split(' ')[0].replace('.', '#'))
    direct.append(d)

all_students = ''

for d in direct:
    d.check_direction_tables()
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:  
        driver.get(d.ref)
        time.sleep(5)  
        soup = BeautifulSoup(driver.page_source, 'html.parser')  
        tag_group = soup.find('div', 'RatingPage_rating__OrcOU')
        all_students = tag_group.find_all('div', 'RatingPage_table__FbzTn')
    for g in range(len(all_students)):
        way = 'abnormal'
        if (g == len(all_students)-1):
            way = 'normal'
        for s in all_students[g]:
            Id = s.find('span')
            number = s.find('p', 'RatingPage_table__position__uYWvi')
            inf = s.find_all('div', 'RatingPage_table__infoLeft__Y_9cA')
            priority = inf[0].find('span')
            score = inf[1].find_all('p')
            own_achive = score[0]
            certificate = s.find_all('div', 'RatingPage_table__info__quwhV')
            if (str(certificate[1]).count('да')): certificate = 1
            else: certificate = 0
            if (len(score) == 1): 
                points = 400
            else:
                points = score[1]
            i = 46
            while(str(number)[i].isdigit()):
                i+=1
            student = Student(str(Id)[6:-7], str(points)[21:-11])
            student.add_to_table('ITMO', d, str(own_achive)[13:-11], int(str(priority)[6:-7]), 1,  str(number)[45:i])
            try:
                points = int(str(points)[21:-11])
            except:
                points = 0
            try:
                own_achive = int(str(own_achive)[13:-11])
            except:
                own_achive = 0
            try:
                Id = int(str(Id)[6:-7])
            except:
                Id = str(Id)[6:-7]
            d.add_to_table_list_line(int(str(number)[45:i]), Id, way, points - own_achive, own_achive, certificate, int(str(priority)[6:-7]))
    print('dist ', d.name,  " complited")


