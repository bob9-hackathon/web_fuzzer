import requests
import xss_result

class XSS:
    def __init__(self, method, attack_url, params,path):
        self.method = method#HTTP METHOD
        self.url = attack_url#공격 대상
        self.par = params#파라미터
        self.seed = open(path, "r")#시드파일 경로

    def StartFuzz(self):
        count = 0
        while True:
            vector = self.seed.readline()#시드 읽기
            print(vector)
            if(vector == ""):
                break
            self.InsertSeed(vector)#@ --> 공격 시드로 변경
            if(self.method == "GET"):
                res = requests.get(self.url, parmas=self.par)
            else:#(self.method == "POST"):
                res = requests.post(self.url, data=self.par)

            self.ResultProcess(res, count)#결과 출력
            count += 1



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

    def ResultProcess(self, res, count):
        #결과 정리
        print("############################################")
        print("            status        suceess       payload     ")
        result_string = "[{number}]     {code}      {suceess}       {payload}       "#번호,응답코드,성공여부,페이로드
        XSSresult = xss_result.XSSresult(self.par, res)
        result_string.format(number=count,code=res.status_code,suceess=XSSresult.FindPayload(),payload=self.par)
        print(result_string)





