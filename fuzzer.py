#!/usr/bin/python


class Fuzzer(object):

    def intro():
        print("################################################");
        print("## Web Fuzzer ##");
        print("박찬솔, 안평주, 석지원, 장재원, 정상훈, 정동현");
        print("################################################");

    
    def __init__(self, url, seed, cookies={}):
        self.url = url
        self.seed = seed
        self.cookies = {}

    def seedfile():
        filepath = open("seed/sql/sql.txt")

        payload_line = filepath.readlines()
        print(payload_line) #test

    seedfile()
