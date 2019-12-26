import uiautomator2 as ut2
from log import Log


class InitDriver:
    def __init__(self, device_name):
        self.device_name = device_name
        self.log = Log()

    # Android
    @property
    def init_driver(self):
        self.log.info("init driver, device_name: %s" % self.device_name)
        try:
            mb = ut2.connect(self.device_name)

            # set default element wait timeout (20 seconds)
            mb.wait_timeout = 20

            # set delay 1s after each UI click and click
            mb.click_post_delay = 1
            self.log.info("connect %s success" % self.device_name)
            return mb

        except Exception as e:
            self.log.info("init driver failed: %s" % e)

    def __str__(self):
        return "<InitDriver>"

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    d2 = ut2.connect("85b531c0")
    d2.app_start("com.sigmob.demo.android")

