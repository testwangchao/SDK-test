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

    driver = InitDriver(device_name="85b531c0")
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
        # todo: check ad is ready
        load_ad_time = get_current_time_stamp(time.time())
        self.__rt(load_ad_time=load_ad_time)
        while 1:
            # todo: 此处通过6号点判断广告是否ready，决定是否调用播放广告
            if time.time() - load_ad_time >= 20:
                raise AdLoadFailed
        # todo: 校验2号点request、respond
        # todo: 校验5号点init、request、respond、loadstart、loadend
        # todo: 校验6号点init、load、ready




if __name__ == '__main__':
    unittest.main()