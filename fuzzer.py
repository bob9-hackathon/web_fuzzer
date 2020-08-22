#!/usr/bin/python3

from requests import *
import requests
import os
import threading
import concurrent.futures

class SQLFuzzer(object):
    
    count = 0

    def __init__(self, url, seedpath):
        self.url = url
        self.seedpath = seedpath
        self.param = param
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count())

    def StartFuzz(self):
        seed_file = open(self.seedpath, "r")
        seed_payloads = seed_file.readlines()
        seed_file.close()
        
        futures = {self.executor.submit(self.fuzzing, seed): seed for seed in seed_payloads}
        for future in concurrent.futures.as_completed(futures):
            self.printresult(future.result())

    def fuzzing(self):
        s = requests.Session()
        loginfo = {"login":"bee", "password":"bug", "security_level" : "0", "form" : "submit"}
        cookie = s.post("http://180.71.77.139"+"/bWAPP/login.php", data=loginfo)
        sess = s.cookies
        requests.get("http://180.71.77.139/bWAPP/sm_local_priv_esc_1.php", cookies=sess)
        phpsessid=sess['PHPSESSID']

        
        for payload in seed_payloads:
            param = {'title':payload, 'action':'search'}
            req = s.get(self.url, params=param, cookies=sess, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            
            status = req.status_code
            url = req.url
            
            print("sql count : ", SQLFuzzer.count)
            print("response status code : ", status)
            print("request url : ", url)
            print("insert payload : ", payload)
            SQLFuzzer.count += 1

    def run(self):
        while True:
            self.fuzzing()

    def printresult(self, result):
        # format: "TYPE, #         Code            Success         Payload"
        SQLFuzzer.count += 1
        result_string = "{:<16}{:<16}{:<16}{}".format("sql#" + str(SQLFuzzer.count), res['http'].status_code, XSSresult.FindPayload(), res['xss'])
        print(result_string)
