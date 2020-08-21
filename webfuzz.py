import os
import requests
import threading
import xss_fuzz

class FUZZER:
    
    def __init__(self):
        self.seed = ""
        self.urls = list()
        self.param_dict = dict()
        self.post_data = dict()
        self.id = 0
    
    def start(self):
        print("Start Fuzzing...\n")
        with requests.Session() as s:
            loginfo = {"login":"bee", "password":"bug", "security_level" : "0", "form" : "submit"}
            s.post(도매인+"/bWAPP/login.php", data=loginfo)
            cookie = s.get(도메인+"/bWAPP/portal.php")
            sess = cookie.cookies
            sess = sess["PHPSESSID"]
            self.fuzzing()
    
    def fuzzing(self):
        for url in self.urls:
            print("Target:", url)
            print("======================================================================")
            print("ID          Response    Lines    Word    Chars    Payload")
            print("======================================================================")

            self.id = 0
            thread_cnt = os.cpu_count()
            threadlist = list()
            # 각 thread에서 뭘 분업할지 고려
            for _ in range(thread_cnt):
                # parameter 전달 순서 고려
                method = ""
<<<<<<< HEAD
                if str(self.post_data) != "None": method.join("POST")
                else: method.join("GET")
                xssfz = xss_fuzz.XSS(method, url, self.param_dict, self.seed)
=======
                if str(self.post_data) != "{}": method = "POST"
                else: method = "GET"
                xssfz = xss_fuzz.XSS(method, url, self.cookie_dict, self.seed)
>>>>>>> f0ba226ac7c18417d6a7986b9cb81941dc4b535e
                thread = threading.Thread(target=xssfz.StartFuzz())
                thread.start()
                threadlist.append(thread)
    
            for thread in threadlist:
                thread.join()
