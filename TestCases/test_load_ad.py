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
from db import Mongo
from log_field import LogField
from tools.utils import parse_log
import exceptions


class LoadAd(unittest.TestCase):

    driver = InitDriver(device_name="85b531c0")
    __d = driver.init_driver
    __op_sdk = Android(driver=__d)
    __dc_log = Dclog()
    __rt = RecordTime()
    __db = Mongo()

    @classmethod
    def setUpClass(cls):
        cls.start_app_time = get_current_time_stamp(time.time())
        print(cls.start_app_time)
        cls.__op_sdk.restart_demo()
        # 获取wmsessionid
        try:
            cls.__wmsessionid = cls.__dc_log.use_tp_get_need_log(cls.start_app_time).get("wmsession_id")
            print(cls.__wmsessionid)
        except exceptions.LogDataError:
            return
        # cls.__db.clear_db()

    def test_play_ad(self):
        __log_field = LogField(wmsession_id=self.__wmsessionid, not_exist_field=["vlist", "load_id"])
        __log_field(attr="test_two_point_request")
        self.__op_sdk.load_ad()
        # todo: check ad is ready
        load_ad_time = int(get_current_time_stamp(time.time())/1000)
        while 1:
            if self.__op_sdk.check_toast("onVideoAdLoadSuccess"):
                break
            if int(get_current_time_stamp(time.time())/1000) - load_ad_time > 45:
                raise AdLoadFailed("广告加载失败")
        # self.assertEqual(self.__op_sdk.get_toast, "onVideoAdPlayStart")
        # todo: 校验2号点request、respond
        # todo: 校验5号点init、request、respond、loadstart、loadend
        # todo: 校验6号点init、load、ready

        for field in __log_field.BASE_FIELD_LIST:
            self.assertIn(field, __log_field.filter_result)
            if field == "carrier":
                continue
            print("%s: %s" % (field, __log_field.filter_result.get(field)))
            self.assertIsNone(__log_field.filter_result.get("field"))

        self.__op_sdk.play_ad()


if __name__ == '__main__':
    unittest.main()