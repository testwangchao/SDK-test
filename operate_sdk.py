from driver import InitDriver
import time
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


if __name__ == '__main__':
    driver = InitDriver(device_name="c6c1b81e")
    d = driver.init_driver
    sdk = OperateSdk(driver=d)
    sdk.driver.app_start("com.sigmob.demo.android")
    sdk.click(text="load dffa3806ae2")
    # todo: check ad is ready by dclog
    time.sleep(5)
    sdk.click(text="play dffa3806ae2")

    if sdk.driver(description="立即下载").exists(timeout=100):
        sdk.driver.xpath(
            '//*[@resource-id="com.sigmob.demo.android:id/dokit_app_contentview_id"]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]').click()
    else:
        print("error")
