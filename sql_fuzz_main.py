#!/usr/bin/python3

from fuzzer import *
import sys

if len(sys.argv) < 2:
    exit("[*] usage python3 sql_fuzz_main.py {url} {seedpath} {param}");

url = sys.argv[1]
seedpath = sys.argv[2]
param = sys.argv[3]

fuzzer = SQLFuzzer(url=url, seedpath=seedpath, param=param) 

fuzzer.run()
