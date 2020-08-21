import argparse
import requests
from bs4 import BeautifulSoup as bs
import webfuzz as wfz
#import xss_fuzz
#import sql_fuzz

def print_introduce():
    print("****************************************************************************")
    print("****************************************************************************")
    print("****************************************************************************")
    print("***                                                                      ***")
    print("***              <<<<<    BOB9_Hackathon_WebFuzzer    >>>>>              ***")
    print("***                                                                      ***")
    print("***              Team. 찬솔곤듀와 다섯난쟁이                               ***")
    print("***              Leader: 박찬솔                                           ***")
    print("***              Member: 석지원, 안평주, 장재원, 정동현, 정상훈             ***")
    print("***                                                                      ***")
    print("****************************************************************************")
    print("****************************************************************************")
    print("****************************************************************************")
    print("\n\n\n")

def add_args(parser):
    parser.add_argument('-seed', required=True, help='퍼징할 시드파일 경로')
    parser.add_argument('-cookies', required=False, help='쿠키값, 여러 개의 쿠키값 구분자: &&&')    
    parser.add_argument('-post', required=False, help='POST 방식으로 넘길 값')             
    parser.add_argument('-urls', required=True, help='대상 주소 URL, 여러 개의 url 구분자: &&&')

def parse_inputs(args, fuzzer):
    
    # seed값 저장
    fuzzer.seed = args.seed

    # url 파싱하여 저장
    if str(args.urls) != "None":
        input_urls = str(args.urls).split("***")
        for url in input_urls:
            fuzzer.urls.append(url)

    # cookie 파싱하여 저장
    if str(args.cookies) != "None":
        input_cookies = str(args.cookies).split("***")
        for cookie in input_cookies:
            equal_parsed = str(cookie).split("=", maxsplit=1)
            fuzzer.cookie_dict[equal_parsed[0]] = equal_parsed[1]                       

    # 입력받은 POST data값 파싱하여 저장
    if str(args.post) != "None":                            
        amp_parsed = str(args.post).split("&")                
        for i in range(len(amp_parsed)):
            equal_parsed = str(amp_parsed[i]).split("=")
            fuzzer.post_data[equal_parsed[0]] = equal_parsed[1]

########################################## </Functions> #########################################


########################################## <Main Loop> ##########################################
if __name__ == "__main__":

    print_introduce()

    # 1. 퍼저 인스턴스 생성
    fuzzer = wfz.FUZZER()

    # 2. argument 등록 및 parsing
    parser = argparse.ArgumentParser(description='사용법')
    add_args(parser)
    args = parser.parse_args()
    parse_inputs(args, fuzzer)

    # 3. fuzzing 시작
    fuzzer.start()

########################################## </Main Loop> ##########################################