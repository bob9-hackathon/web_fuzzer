#!/usr/bin/python3

from fuzzer import *
import sys

if len(sys.argv) < 2:
    exit("[*] usage python3 sql_fuzz_main.py {url} {seedpath}");

url = sys.argv[1]

seedpath = sys.argv[2]

fuzzer = SQLFuzzer(url=url, seedpath=seedpath, param=param) 

fuzzer.run()
