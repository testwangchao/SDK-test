import uiautomator2 as ut2
from tools.loggers import JFMlogging

log = JFMlogging().getloger()


class InitDriver:

    def __init__(self, device_name):
        self.device_name = device_name

    # Android
    @property
    def init_driver(self):
        log.info("init driver, device_name: %s" % self.device_name)
        try:
            mb = ut2.connect(self.device_name)

            # set default element wait timeout (20 seconds)
            mb.wait_timeout = 20

            # set delay 1s after each UI click and click
            mb.click_post_delay = 1
            log.info("connect %s success" % self.device_name)
            return mb

        except Exception as e:
            log.info("init driver failed: %s" % e)