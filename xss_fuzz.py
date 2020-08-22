import os
import requests
import threading
import concurrent.futures
import xss_result

class XSS:

    count = 0

    def __init__(self, method, attack_url, params,path):
        self.method = method#HTTP METHOD
        self.url = attack_url#공격 대상
        self.par = params#파라미터
        self.seed = open(path, "r")#시드파일 경로
        tmp = self.seed.readlines()
        self.seed.close()
        self.seed = tmp
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count())
    
    
    def StartFuzz(self):
        futures = {self.executor.submit(self.Fuzz, vector): vector for vector in self.seed}
        for future in concurrent.futures.as_completed(futures):
            self.ResultProcess(future.result())#결과 출력
    
    def Fuzz(self, vector):
        if(self.method == "GET"):
            res = requests.get(self.url, params=self.InsertSeed(vector))#@ --> 공격 시드로 변경
        else:#(self.method == "POST"):
            res = requests.post(self.url, data=self.InsertSeed(vector))#@ --> 공격 시드로 변경
        
        return res


    def InsertSeed(self, vector):
        #파라미터마다 다른 시드 삽입
        temp = self.par
        for i in temp.keys():
            if(temp[i] == '@'):
                temp[i] = vector
        return temp

        # 파라미터에 서로 같은 시드
        # tmp = self.seed.readline()
        # for i in self.par.keys():
        #     if(self.par[i] == '@'):
        #         self.par[i] = tmp

    def ResultProcess(self, res):
        # 결과 정리
        # format: "TYPE, #         Code            Success         Payload"
        XSSresult = xss_result.XSSresult(self.par, res)
        XSS.count += 1
        result_string = "{:<16}{:<16}{:<16}{}".format("xss#" + XSS.count, res.status_code, XSSresult.FindPayload(), self.par)
        print(result_string)