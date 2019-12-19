from operate_sdk import OperateSdk
from driver import InitDriver


class Android(OperateSdk):
    LOAD_AD = "load dffa3806ae2"
    PLAY_AD = "play dffa3806ae2"
    CLOSE_BUTTON = "//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]"
    CLICK_BUTTON = "立即下载"
    SKIP_BUTTON = "skip"
    CONFIRM_CLOSE_BUTTON = "确定关闭"

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

    #
    def click_confirm_close_button(self):
        self.click(self.CONFIRM_CLOSE_BUTTON)


if __name__ == '__main__':
    from uiautomator2.watcher import Watcher
    import time
    __driver = InitDriver(device_name="127.0.0.1:62002").init_driver
    an = Android(driver=__driver)
    try:
        __driver.app_uninstall("com.tencent.android.qqdownloader")
    except Exception as e:
        print(e)
    __driver.app_stop("com.sigmob.demo.android")
    __driver.app_start("com.sigmob.demo.android")
    print(__driver.serial)
    watchers = Watcher(__driver)
    # print(watchers.when("总是允许").click())
    #
    # watchers("next").when("取消").when("下一步").click()
    # watchers.when("完成").click()
    # __driver.watcher(name="install finish back to demo").when(text="完成").press("back")
    # __driver.watcher(name="accept permissions").watched=True
    # __driver.watcher(name="install").watched=True
    # __driver.watcher(name="install finish back to demo").watched=True
    # __driver.watcher(name="accept permissions")
    # watchers.start(2)  # 默认每4s检查一次
    # print(__driver.watcher)
    an.load_ad()
    toast_msg = None
    while 1:
        toast_msg = an.driver.toast.get_message(wait_timeout=1, cache_timeout=5)
        if toast_msg == "onVideoAdLoadSuccess":
            break
    an.play_ad()
    click_button_time = time.time()
    while 1:
        if time.time() - click_button_time > 8:
            an.click_skip_button()
            time.sleep(1)
            an.click_confirm_close_button()
            break
    # while 1:
    #     toast_msg = an.driver.toast.get_message(wait_timeout=1, cache_timeout=5)
    #     print(toast_msg)
    #     if toast_msg == "onVideoAdPlayEnd":
    #         an.click_button()
    time.sleep(2)
    an.click_button()
    while 1:
        watchers("next to install").when("取消").when("下一步").click()
        watchers("install").when("取消").when("安装").click()
        watchers.run()
        if __driver(text="安装").exists():
            watchers.remove("next to install")
        if __driver(text="打开").exists() and __driver(text="打开").exists():
            watchers.remove("install")
            __driver(text="完成").click()
            break
    time.sleep(1)
    an.click_close_button()
    print("hello world")
