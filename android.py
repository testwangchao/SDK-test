from operate_sdk import OperateSdk
from driver import InitDriver


class Android(OperateSdk):
    LOAD_AD = "load dffa3806ae2"
    PLAY_AD = "play dffa3806ae2"
    CLOSE_BUTTON = "'//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]'"
    CLICK_BUTTON = ""
    SKIP_BUTTON = "skip"

    def __init__(self, driver):
        super(Android, self).__init__(driver)

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
    __driver = InitDriver(device_name="127.0.0.1:62001").init_driver
    an = Android(driver=__driver, name="wangchao")
    print(an.name)
    an.click('''//*[@resource-id="com.android.browser:id/url"]''')