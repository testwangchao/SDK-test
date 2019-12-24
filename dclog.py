import json
import requests
from db import Mongo
import exceptions


class Dclog:

    __URL = ""
    __db = Mongo()

    def __init__(self):
        self.filter_para = None
        self.log_url = self.__URL.format(json.dumps(self.filter_para))

    def __call__(self, para, **kwargs):
        self.filter_para = para
        if kwargs.get("recored_time"):
            self.current_time = kwargs.get("recored_time")

    def check_category(self):
        log_result = requests.get(self.log_url).text

    # 通过请求开屏的2号点获取，与启动应用记录的时间做比较，获得当前的wmsession_id
    def use_tp_get_need_log(self, record_time):
        '''
        以record_time为分界，过滤打点
        :param record_time: 指定的时间
        :return: dict
        '''
        # 等于使用 ==
        filter_data = {"_ac_type": "2", "category": "request", "adtype": "2"}
        filter_data.update({"$where": "function() {return this.timestamp>%s}" % record_time})
        data = self.__db.find_all(sort_way=-1, field="timestamp", filter=filter_data)
        if data.count() == 1:
            return data[0]
        else:
            raise exceptions.LogDataError

    # 根据5号点respond获取request_id
    # def


if __name__ == '__main__':
    db = Dclog()
    try:
        print(db.use_tp_get_need_log(record_time=1577182834327))
    except exceptions.LogDataError as e:
        print(11111)