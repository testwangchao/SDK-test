import time
import unittest
import sys
sys.path.append("..")
from driver import InitDriver
from dclog import Dclog
from utils import get_current_time_stamp
from android import Android
from exceptions import AdLoadFailed
from db import Mongo
import exceptions
from utils import all_paras
from log import Log


class LoadAd(unittest.TestCase):

    driver = InitDriver(device_name="c6c1b81e")
    __d = driver.init_driver
    __op_sdk = Android(driver=__d)
    __db = Mongo()
    __log = Log()

    @classmethod
    def setUpClass(cls):
        cls.start_app_time = get_current_time_stamp(time.time())
        cls.__log.info("启动demo时间为：%s" % cls.start_app_time)
        cls.__op_sdk.restart_demo()
        # 获取wmsessionid
        try:
            cls.__wmsessionid = cls.__db.use_tp_get_need_log(cls.start_app_time).get("wmsession_id")
        except exceptions.LogDataError:
            return
        cls.__log.info("wmsessionid为：%s" % cls.__wmsessionid)
        cls.__dc_log = Dclog(cls.__wmsessionid)

    @classmethod
    def tearDownClass(cls):
        cls.__db.clear_db()
        cls.__log.info("本地数据库已清空")

    def test_play_ad(self):
        self.__log.info("加载广告")
        self.__op_sdk.load_ad()
        load_ad_time = int(get_current_time_stamp(time.time())/1000)
        while 1:
            if self.__op_sdk.check_toast("onVideoAdLoadSuccess"):
                self.__log.info("广告加载完成")
                time.sleep(5)
                break
            if int(get_current_time_stamp(time.time())/1000) - load_ad_time > 45:
                self.__log.info("广告加载失败")
                raise AdLoadFailed("广告加载失败")
            if self.__op_sdk.check_toast('''onVideoAdLoadError error: [[ 200000 ] [{"sigmob":{"errorCode":600104,"message":"文件下载错误"}}]]'''):
                raise AdLoadFailed("广告加载失败")
            if self.__op_sdk.check_toast('''onVideoAdLoadError error: [[ 200000 ] [{"sigmob":{"errorCode":200000,"message":"广告无填充"}}]]'''):
                raise AdLoadFailed("广告无填充")
        # self.assertEqual(self.__op_sdk.get_toast, "onVideoAdPlayStart")
        # todo: 校验2号点request、respond
        # todo: 校验5号点init、request、respond、loadstart、loadend
        # todo: 校验6号点init、load、ready
        for para in all_paras:
            for k in para:
                value = para.get(k)
                if isinstance(value, dict):
                    self.__log.info(k)
                    for key in value:
                        self.__dc_log[key] = value.get(key)
            self.__log.info(self.__dc_log.filter_para)
            search_result = self.__dc_log.parse_log(para=self.__dc_log.filter_para)
            self.__log.info("")
            self.assertEqual(1, len(search_result))
            data = self.__dc_log.remove_field(remove_lt=para.get("remove_lt", None), need_list=para.get("need_list", None))
            for field in data:
                self.assertIn(field, search_result[0])
                if field == "carrier":
                    continue
                self.assertIsNotNone(search_result[0].get(field))

        # self.__op_sdk.play_ad()


if __name__ == '__main__':
    unittest.main()