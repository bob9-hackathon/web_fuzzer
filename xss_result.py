from selenium import webdriver

class XSSresult:
    def __init__(self, params, res):
        self.par = params
        self.res = res

    def FindPayload(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:/chromedriver.exe')
        try:
            html = self.res.text
            
            html = "<script>location.reload = () => {}; window.testSuccess = false; window.executeTest = () => testSuccess = true;</script>" + html
            driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html))
            ret = driver.execute_script('return window.testSuccess')
            if ret:
                return 'OK'
            else: 
                return 'NO'
        except:
            return 'NO'
        finally:
            driver.quit()
