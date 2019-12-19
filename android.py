from operate_sdk import OperateSdk
from driver import InitDriver


class Android(OperateSdk):
    LOAD_AD = "load dffa3806ae2"
    PLAY_AD = "play dffa3806ae2"
    CLOSE_BUTTON = "'//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]'"
    CLICK_BUTTON = "立即下载"
    SKIP_BUTTON = "skip"

    def __init__(self, driver):
        super(Android, self).__init__(driver)
        self.driver = driver

    # load ad
    def load_ad(self):
        self.click(self.LOAD_AD)

    # play ad
    def play_ad(self):
        self.click(self.PLAY_AD)

    # click close button
    def click_close_button(self):
        self.click(self.CLOSE_BUTTON)

    # click download button or jump to web page
    def click_button(self):
        self.click(self.CLICK_BUTTON)

    # skip button
    def click_skip_button(self):
        self.click(self.SKIP_BUTTON)


if __name__ == '__main__':

    import time
    __driver = InitDriver(device_name="85b531c0").init_driver
    an = Android(driver=__driver)
    __driver.app_start("com.sigmob.demo.android")
    __driver.xpath.when("总是允许").click()
    __driver.xpath.when("安装").click()
    __driver.xpath.when("完成").click()
    # __driver.watcher(name="install finish back to demo").when(text="完成").press("back")
    # __driver.watcher(name="accept permissions").watched=True
    # __driver.watcher(name="install").watched=True
    # __driver.watcher(name="install finish back to demo").watched=True
    # __driver.watcher(name="accept permissions")
    __driver.xpath.watch_background()  # 默认每4s检查一次

    an.load_ad()
    toast_msg = None
    while 1:
        toast_msg = an.driver.toast.get_message(wait_timeout=1, cache_timeout=5)
        if toast_msg == "onVideoAdLoadSuccess":
            break
    print(toast_msg)
    an.play_ad()
    while 1:
        toast_msg = an.driver.toast.get_message(wait_timeout=1, cache_timeout=5)
        print(toast_msg)
        if toast_msg == "onVideoAdPlayEnd":
            an.click_button()