import threading

class FUZZER:
    def __init__(self):
        self.seed = ""
        self.urls = list()
        self.cookie_dict = dict()
        self.post_data = dict()
        self.ID = 0
    
    def start(self):
        print("Start Fuzzing...\n")
        self.fuzzing()
    
    def fuzzing(self):
        for url in self.urls:
            print("Target :", url)
            print("======================================================================")
            print("ID          Response    Lines    Word    Chars    Payload")
            print("======================================================================")

            thread_cnt = len(self.cookie_dict)
            threadlist = list()
            for _ in range(thread_cnt):
                #스레드에서 call 하는 부분 수정 필요
                thread = threading.Thread(target=self.print_res, args=(self.seed, url, self.cookie_dict, self.post_data))
                thread.start()
                threadlist.append(thread)
    
            for thread in threadlist:
                thread.join()
    # 나중에 수정할 부분
    def print_res(self, Response, Lines, Word, Chars, Payload):
        print("{:<12}{:<12}{:<9}{:<8}{:<9}{}".format(self.ID, Response, Lines, Word, Chars, Payload))