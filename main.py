import os
import sys
import argparse                         # 인자값을 쉽게 옵션으로 만들 수 있는 라이브러리
import requests                         # HTTP요청을 할 수 있는 라이브러리
import threading
import time
from bs4 import BeautifulSoup as bs     # html 코드를 Python이 이해하는 객체 구조로 변환하는 Parsing

# 입력받은 url 저장
urls = list()

# 입력받은 쿠키값 저장
cookie_dict = dict()

# 입력받은 POST data값 저장
post_data = dict()

# Payload의 개수 세는 변수
ID = 0

########################################## <Functions> ##########################################
def print_introduce():
    print("****************************************************************************\n")
    print("****************************************************************************\n")
    print("****************************************************************************\n")
    print("***                                                                      ***\n")
    print("***              <<<<<    BOB9_Hackathon_WebFuzzer    >>>>>              ***\n")
    print("***                                                                      ***\n")
    print("***              Team. 찬솔곤듀와 다섯난쟁이                               ***\n")
    print("***              Leader: 박찬솔                                           ***\n")
    print("***              Member: 석지원, 안평주, 장재원, 정동현, 정상훈             ***\n")
    print("***                                                                      ***\n")
    print("****************************************************************************\n")
    print("****************************************************************************\n")
    print("****************************************************************************\n")
    print("\n\n\n")

def add_args(parser):
    parser.add_argument('-seed', required=True, help='퍼징할 시드파일 경로')
    parser.add_argument('-cookies', required=False, help='쿠키값, 여러 개의 쿠키값 구분자: &&&')    
    parser.add_argument('-post', required=False, help='POST 방식으로 넘길 값')             
    parser.add_argument('-urls', required=True, help='대상 주소 URL, 여러 개의 url 구분자: &&&')

def parse_inputs(args):
    
    # url 파싱
    if str(args.urls) != "None":
        input_urls = str(args.cookie).split("&&&")
        for url in input_urls:
            urls.append(url)

    # cookie 파싱
    if str(args.cookie) != "None":
        input_cookies = str(args.cookie).split("&&&")
        for cookie in input_cookies:
            equal_parsed = str(cookie).split("=", maxsplit=1)
            cookie_dict[equal_parsed[0]] = equal_parsed[1]                       

    # 입력받은 POST data값 파싱하여 저장
    if str(args.post) != "None":                            # post data가 비어있지 않을 경우(입력 받았을 경우)
        amp_parsed = str(args.post).split("&")                    # "&"을 기준으로 post를 쪼갬
        for i in range(len(amp_parsed)):                          # 입력받은 data만큼 반복
            equal_parsed = str(amp_parsed[i]).split("=")                  # "="을 기준으로 data를 쪼갬
            post_data[equal_parsed[0]] = equal_parsed[1]                     # 쪼갠 data를 dictionary형태로 저장

def webfuzz(seed, url, cookies, posts):
    print("Target :", url)
    print("======================================================================\n")
    print("ID          Response    Lines    Word    Chars    Payload")
    print("======================================================================\n")

########################################## </Functions> #########################################


########################################## <Main Loop> ##########################################
if __name__ == "__main__":

    print_introduce()

    # 1. argument 등록
    parser = argparse.ArgumentParser(description='사용법')
    add_args(parser)
    arguments = parser.parse_args()

    # 2. 입력받은 인자값 파싱
    parse_inputs(arguments)

    # 3. 멀티스레드로 구현
    thread_cnt = len(cookie_dict)
    threadlist = list()
    for i in range(thread_cnt):
        thread = threading.Thread(target=webfuzz,args=(arguments.seed, arguments.url, cookie_dict, post_data))
        thread.start()
        threadlist.append(thread)
    
    for thread in threadlist:
        thread.join()

########################################## </Main Loop> ##########################################