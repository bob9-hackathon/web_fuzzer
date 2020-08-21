class XSSresult:
    def __init__(self, params, res):
        self.par = params
        self.res = res

    def FindPayload(self):
        html = self.res.text
        key = self.par.keys()
        if html in self.par[key[0]]:
            return "OK"
        else:
            return "NO"
