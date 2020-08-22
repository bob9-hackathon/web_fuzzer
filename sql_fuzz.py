#!/usr/bin/python3
import requests
import os
import threading
import concurrent.futures

class SQLFuzzer(object):

    count = 0

    def __init__(self, url, seedpath, cookie):
        self.url = url
        self.seedpath = seedpath
        self.cookie = cookie
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count())
    
    def StartFuzz(self):
        print(self.seedpath)
        seed_file = open(self.seedpath, "r")
        seed_payloads = seed_file.readlines()
        seed_file.close()

        s = requests.Session()
        loginfo = {"login":"bee", "password":"bug", "security_level" : "0", "form" : "submit"}
        cookie = s.post("http://180.71.77.139"+"/bWAPP/login.php", data=loginfo)
        sess = s.cookies
        phpsessid=sess['PHPSESSID']

        futures = {self.executor.submit(self.fuzzing, s, seed, sess): seed for seed in seed_payloads}
        for future in concurrent.futures.as_completed(futures):
            self.printres(future.result())
    
    def fuzzing(self, s, payload, sess):

            param = {'title':payload, 'action':'search'}
            req = s.get(self.url, params=param, cookies=sess, headers={'Content-Type': 'application/x-www-form-urlencoded'})

            status = req.status_code
            url = req.url

            result = list(status, "?", payload)
            return result

    def printres(self, result):
        SQLFuzzer.count += 1
        result_string = "{:<16}{:<16}{:<16}{}".format("xss#" + str(SQLFuzzer.count), result[0], result[1], result[2])
        print(result_string)