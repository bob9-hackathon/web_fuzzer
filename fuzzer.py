#!/usr/bin/python3

import requests

class SQLFuzzer(object):

    def __init__(self, url, seedpath, cookies={}):
        self.url = url
        self.seedpath = seedpath
        self.cookies = {}

    def login(self):
        s = requests.Session()
        loginfo = {"login":"bee", "password":"bug", "security_level" : "0", "form" : "submit"}
        s.post("http://180.71.77.139/bWAPP/login.php", data=loginfo)
        cookie = s.get("http://180.71.77.139/bWAPP/portal.php")
        sess = cookie.cookies
        sess = sess["PHPSESSID"]
        print(sess)

    def parser(self):
        seed_file = open(self.seedpath, "r")
        seed_payloads = seed_file.readlines()
        for seed_payload in seed_payloads:
            print(seed_payload)

    def fuzzing(self):
        print("mycode...git..pull")

    def run(self):
        self.parser()
        self.login()

    
