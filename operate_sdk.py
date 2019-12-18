from driver import InitDriver
import time
import re
import requests


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


if __name__ == '__main__':
    driver = InitDriver(device_name="85b531c0")
    d = driver.init_driver
    sdk = OperateSdk(driver=d)
    sdk.driver.app_start("com.sigmob.demo.android")
    sdk.click("load dffa3806ae2")
    # todo: check ad is ready by dclog
    time.sleep(5)
    sdk.click("play dffa3806ae2")
    # try:
    #     if sdk.driver(text="立即下载").exists(timeout=50):
    #         sdk.driver.xpath('//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]').click()
    # except requests.ReadTimeout:
    #     if sdk.driver(description="立即下载").exists(timeout=50):
    #         sdk.driver.xpath('//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]').click()
    while 1:
        if sdk.driver(text="立即下载1111").exists():
            print(sdk.driver(text="立即下载").exists())
            sdk.driver.xpath('//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]').click()
        elif sdk.driver(description="立即下载").exists(timeout=50):
            sdk.driver.xpath('//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]').click()