#!/usr/bin/python3

from requests import *
import requests

class SQLFuzzer(object):

    def __init__(self, url, seedpath, param):
        self.url = url
        self.seedpath = seedpath
        self.param = param

    def fuzzing(self):
        seed_file = open(self.seedpath, "r")
        seed_payloads = seed_file.readlines()

        for seed_payload in seed_payloads:
            data = seed_payload

        s = requests.Session()
        loginfo = {"login":"bee", "password":"bug", "security_level" : "0", "form" : "submit"}
        cookie = s.post("http://180.71.77.139"+"/bWAPP/login.php", data=loginfo)
        sess = s.cookies
        requests.get("http://180.71.77.139/bWAPP/sm_local_priv_esc_1.php", cookies=sess)
        phpsessid=sess['PHPSESSID']
        print(phpsessid)

        # test send data
        param = {'title':data, 'action':'search'}
        req = s.get(self.url, params=param, cookies=sess)
        res = req.text
        url = req.url
        print(res)
        print(url)

    #def seed(self, seed_payload):

    def run(self):
        self.fuzzing()
    
