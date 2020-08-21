import requests
import xss_result

class XSS:
    def __init__(self, method, attack_url, params,path):
        self.method = method#HTTP METHOD
        self.url = attack_url#공격 대상
        self.par = params#파라미터
        self.seed = open(path, "r")#시드파일 경로
        tmp = self.seed.readlines()
        self.seed.close()
        self.seed = tmp
    def StartFuzz(self):
        count = 0
        for vector in self.seed:
            if(self.method == "GET"):
                res = requests.get(self.url, params=self.InsertSeed(vector))#@ --> 공격 시드로 변경
            else:#(self.method == "POST"):
                res = requests.post(self.url, data=self.InsertSeed(vector))#@ --> 공격 시드로 변경

            self.ResultProcess(res, count)#결과 출력
            count += 1

    def InsertSeed(self, vector):
        #파라미터마다 다른 시드 삽입
        temp = self.par;
        for i in temp.keys():
            if(temp[i] == '@'):
                temp[i] = vector
        return temp

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
        print(result_string.format(number=count,code=res.status_code,suceess=XSSresult.FindPayload(),payload=self.par))





