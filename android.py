from operate_sdk import OperateSdk
from driver import InitDriver
from install_element import WatchInstall
import time


class Android(OperateSdk):
    LOAD_AD = "load dffa3806ae2"
    PLAY_AD = "play dffa3806ae2"
    CLOSE_BUTTON = "//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]"
    CLICK_BUTTON = "立即下载"
    SKIP_BUTTON = "skip"
    CONFIRM_CLOSE_BUTTON = "确定关闭!"
    CONTINUE_PLAY_AD = "继续播放"

    def __init__(self, driver):
        super(Android, self).__init__(driver)
        self.driver = driver
        self.is_ready = False

    def __call__(self, driver, **kwargs):
        __watchers = WatchInstall(driver)
        return __watchers

    def __str__(self):
        return "<OperateSdk>"

    def __repr__(self):
        return str(self)

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

    # click the confirm close video button
    def click_confirm_close_button(self):
        self.click(self.CONFIRM_CLOSE_BUTTON)

    # check toast
    def check_toast(self, expect_toast):
        print(self.get_toast)
        if expect_toast == self.get_toast:
            return True
        return False

    # get toast
    @property
    def get_toast(self):
        return self.driver.toast.get_message()

    # uninstall apk exist in device
    def uninstall_exist_apk(self, package):
        try:
            self.driver.app_uninstall(package)
        except Exception as e:
            return e

    # apk install finish back to demo
    def install_finished_back(self):
        while 1:
            pass

    # stop demo and restart demo
    def restart_demo(self):
        self.driver.app_stop("com.sigmob.demo.android")
        self.driver.app_start("com.sigmob.demo.android")
        time.sleep(7)


if __name__ == '__main__':
    from uiautomator2.watcher import Watcher

    __driver = InitDriver(device_name="85b531c0").init_driver
    an = Android(driver=__driver)
    __driver.app_stop("com.sigmob.demo.android")
    __driver.app_start("com.sigmob.demo.android")
    watchers = Watcher(__driver)

    an.load_ad()
    toast_msg = None
    while 1:
        s = an.driver
        toast_msg = s.toast.get_message(wait_timeout=1, cache_timeout=5)
        print(toast_msg)
        if toast_msg == "onVideoAdLoadSuccess":
            break
    an.play_ad()
    # todo：better way click_button_time：开始播放回调的时间
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

    simulator = an(__driver).samsung()
    while 1:
        if __driver(text="完成").exists() and __driver(text="打开").exists():
            __driver(text="完成").click()
            try:
                __driver.app_uninstall("com.tencent.android.qqdownloader")
            except Exception as e:
                print(e)
            break
    an.click_close_button()
    print("hello world")
    an(__driver).stop_watch()
