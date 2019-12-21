import re


class OperateSdk:
    def __init__(self, driver):
        self.driver = driver
        
    def click(self, element):
        if re.findall("下载", element) or re.findall("详情", element):
            self.driver(text=element).click()
        elif re.findall("//", element):
            self.driver.xpath(element).click()
        elif re.findall("skip", element):
            self.driver(description="skip").click()
        else:
            self.driver(text=element).click()

