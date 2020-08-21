import threading
import xss_fuzz

class FUZZER:
    def __init__(self):
        self.seed = ""
        self.urls = list()
        self.cookie_dict = dict()
        self.post_data = dict()
        self.ID = 0
    
    def start(self):
        print("Start Fuzzing...\n")
        self.fuzzing()
    
    def fuzzing(self):
        for url in self.urls:
            print("Target :", url)
            print("======================================================================")
            print("ID          Response    Lines    Word    Chars    Payload")
            print("======================================================================")

            thread_cnt = len(self.cookie_dict)
            threadlist = list()
            for _ in range(thread_cnt):
                # parameter 전달 순서 고려
                method = ""
                if str(self.post_data) != "{}": method = "POST"
                else: method = "GET"
                xssfz = xss_fuzz.XSS(method, url, self.cookie_dict, self.seed)
                thread = threading.Thread(target=xssfz.StartFuzz())
                thread.start()
                threadlist.append(thread)
    
            for thread in threadlist:
                thread.join()
    # 나중에 수정할 부분
    def print_res(self, Response, Lines, Word, Chars, Payload):
        print("{:<12}{:<12}{:<9}{:<8}{:<9}{}".format(self.ID, Response, Lines, Word, Chars, Payload))