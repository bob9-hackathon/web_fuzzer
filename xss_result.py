from selenium import webdriver

class XSSresult:
    def __init__(self, params, res):
        self.par = params
        self.res = res

    def FindPayload(self):
        html = self.res.text
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(chrome_options=chrome_options)
        
        html = "<script>location.reload = () => {}; window.testSuccess = false; window.executeTest = () => testSuccess = true;</script>" + html
        driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html))
        if driver.execute_script('return window.testSuccess'):
            return 'OK'
        else: 
            return 'NO'
