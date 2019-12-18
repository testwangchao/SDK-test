import time
import unittest
import sys
sys.path.append("..")
from operate_sdk import OperateSdk
from driver import InitDriver
from dclog import Dclog
from tools.utils import get_current_time_stamp
from record_time import RecordTime


class LoadAd(unittest.TestCase):

    driver = InitDriver(device_name="85b531c0")
    __d = driver.init_driver
    __op_sdk = OperateSdk(driver=__d)
    __dc_log = Dclog()
    __rt = RecordTime()

    @classmethod
    def setUpClass(cls):
        cls.__op_sdk.driver.app_start("com.sigmob.demo.android")
        cls.__rt(app_start_tp=get_current_time_stamp(time.time()))
        print(cls.__rt.current_time)

    def test_load_ad(self):
        self.__op_sdk.click("load dffa3806ae2")


if __name__ == '__main__':
    unittest.main()