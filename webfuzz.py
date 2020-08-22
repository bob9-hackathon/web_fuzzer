import requests
import xss_fuzz
#import sql_fuzz

class FUZZER:
    
    def __init__(self):
        self.seed = ""
        self.urls = list()
        self.param_dict = dict()
        self.post_data = dict()
        self.cookie = dict()
    
    def start(self):
        print("Start Fuzzing...\n")
        self.fuzzing()
    
    def fuzzing(self):
        for url in self.urls:

            print("Target:", url)
            print("=============================================================")
            print("TYPE, #         Code            Success         Payload")
            print("=============================================================")

            method = ""
            if str(self.post_data) != "{}": method = "POST"
            else: method = "GET"
            xssfz = xss_fuzz.XSS(method, url, self.param_dict, self.seed)
            xssfz.StartFuzz()

            #sqlfz = sql_fuzz.SQLFuzzer(url, self.seed, param_dict)
            #sqlfz.StartFuzz()