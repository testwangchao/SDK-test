import time
import unittest
import sys
sys.path.append("..")
from driver import InitDriver
from dclog import Dclog
from tools.utils import get_current_time_stamp
from record_time import RecordTime
from android import Android
from exceptions import AdLoadFailed


class LoadAd(unittest.TestCase):

    driver = InitDriver(device_name="127.0.0.1:62001")
    __d = driver.init_driver
    __op_sdk = Android(driver=__d)
    __dc_log = Dclog()
    __rt = RecordTime()

    @classmethod
    def setUpClass(cls):
        cls.__op_sdk.driver.app_start("com.sigmob.demo.android")
        cls.__rt(app_start_tp=get_current_time_stamp(time.time()))
        # todo: get wmsessionid
        cls.__wmsessionid = None

    def test_load_ad(self):
        self.__op_sdk.load_ad()
        self.assertEqual(self.__op_sdk.get_toast, "onVideoAdLoadSuccess")
        # todo: 校验打点

    def test_play_ad(self):
        self.__op_sdk.load_ad()
        # todo: check ad is ready
        load_ad_time = get_current_time_stamp(time.time())
        if self.__op_sdk.check_toast("onVideoAdLoadSuccess"):
            self.__op_sdk.play_ad()
        else:
            raise AdLoadFailed("广告加载失败")
        self.assertEqual(self.__op_sdk.get_toast, "onVideoAdPlayStart")
        # todo: 校验2号点request、respond
        # todo: 校验5号点init、request、respond、loadstart、loadend
        # todo: 校验6号点init、load、ready


if __name__ == '__main__':
    unittest.main()