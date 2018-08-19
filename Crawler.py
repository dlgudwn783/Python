import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
driver = webdriver.Chrome('/Users/Mythic Dawn/untitled/Crawler/chromedriver')
lst_pos = []
lst_neg = []
for days in range(int(input("시작일을 입력하십시오: ")), int(input("종료일을 입력하십시오: "))+1):
    if days < 10:
        url = 'http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=100&date=2018070{}'.format(days)
        resp = requests.get(url)
        sleep(1)
        html_ranking = resp.text
        soup = BeautifulSoup(html_ranking, 'lxml')
        result = soup.select('div.ranking_headline > a')
        for href in result:
            head_url = 'http://news.naver.com'+href.get('href')
            html_headline = driver.get(head_url)
            sleep(1)
            like = driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.good > a > span.u_likeit_list_count._count')
            warm = driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.warm > a > span.u_likeit_list_count._count')
            sad = driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.sad > a > span.u_likeit_list_count._count')
            angry = driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.angry > a > span.u_likeit_list_count._count')
            parsed_like = re.sub('[-=.#/?:$},]', '', like.text)
            parsed_warm = re.sub('[-=.#/?:$},]', '', warm.text)
            parsed_sad = re.sub('[-=.#/?:$},]', '', sad.text)
            parsed_angry = re.sub('[-=.#/?:$},]', '', angry.text)
            lst_pos.append(int(parsed_like))
            lst_pos.append(int(parsed_warm))
            lst_neg.append(int(parsed_sad))
            lst_neg.append(int(parsed_angry))
    elif days >= 10:
        url = 'http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=100&date=201807{}'.format(days)
        resp = requests.get(url)
        sleep(1)
        html_ranking = resp.text
        soup = BeautifulSoup(html_ranking, 'lxml')
        result = soup.select('div.ranking_headline > a')
        for href in result:
            head_url = 'http://news.naver.com'+href.get('href')
            html_headline = driver.get(head_url)
            sleep(1)
            like = driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.good > a > span.u_likeit_list_count._count')
            warm = driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.warm > a > span.u_likeit_list_count._count')
            sad = driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.sad > a > span.u_likeit_list_count._count')
            angry = driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.angry > a > span.u_likeit_list_count._count')
            parsed_like = re.sub('[-=.#/?:$},]', '', like.text)
            parsed_warm = re.sub('[-=.#/?:$},]', '', warm.text)
            parsed_sad = re.sub('[-=.#/?:$},]', '', sad.text)
            parsed_angry = re.sub('[-=.#/?:$},]', '', angry.text)
            lst_pos.append(int(parsed_like))
            lst_pos.append(int(parsed_warm))
            lst_neg.append(int(parsed_sad))
            lst_neg.append(int(parsed_angry))

results = sum(lst_pos)/(sum(lst_pos)+sum(lst_neg))*100
print("총 공감 대비 긍정적 공감의 비율은", results, "% 입니다.")
