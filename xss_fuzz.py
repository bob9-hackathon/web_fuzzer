import requests

class XSS:
    def __init__(self, method, attack_url, params,path):
        self.method = method
        self.url = attack_url
        self.par = params
        self.seed = open(path, "r")

    def StartFuzz(self):
        while True:
            vector = self.seed.readline()
            if(vector == ""):
                break
            self.InsertSeed(vector)#@ --> 공격 시드로 변경
            if(self.method == "GET"):
                requests.get(self.url, parmas=self.par)
            elif(self.method == "POST"):
                requests.post(self.url, data=self.par)

    def InsertSeed(self, vector):
        #파라미터마다 다른 시드 삽입
        for i in self.par.keys():
            if(self.par[i] == '@'):
                self.par[i] = self.seed.readline()

        # 파라미터에 서로 같은 시드
        # tmp = self.seed.readline()
        # for i in self.par.keys():
        #     if(self.par[i] == '@'):
        #         self.par[i] = tmp
    def ResultProcess(self, res):
        #결과 정리




