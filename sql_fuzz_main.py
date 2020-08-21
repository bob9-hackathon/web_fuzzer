#!/usr/bin/python3

from fuzzer import *
import sys

if len(sys.argv) < 2:
    exit("[*] usage python3 sql_fuzz_main.py {url} {seedpath} {cookies}");

url = sys.argv[1]
seedpath = sys.argv[2]
cookies = sys.argv[3]

fuzzer = SQLFuzzer(url=url, seedpath=seedpath, cookies=cookies) 

fuzzer.run()
