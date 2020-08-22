import requests
import xss_fuzz
#import sql_fuzz

class FUZZER:
    
    def __init__(self):
        self.seed = ""
        self.urls = list()
        self.param_dict = dict()
        self.post_data = dict()
    
    def start(self):
        print("Start Fuzzing...\n")
        self.fuzzing()
    
    def fuzzing(self):
        for url in self.urls:
            #로그인 스크립트
            domain = url[:url.find('/', url.find("//") + 2)]
            s = requests.Session()
            loginfo = {"login":"bee", "password":"bug", "security_level" : "0", "form" : "submit"}
            s.post(domain+"/bWAPP/login.php", data=loginfo)
            sess = s.cookies
            sess = sess["PHPSESSID"]

            print("Target:", url)
            print("=============================================================")
            print("TYPE, #         Code            Success         Payload")
            print("=============================================================")

            method = ""
            if str(self.post_data) != "{}": method = "POST"
            else: method = "GET"
            xssfz = xss_fuzz.XSS(method, url, self.param_dict, self.seed)
            xssfz.StartFuzz()

            #sqlfz 부분 추가