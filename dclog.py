import json
from lxml import etree
import requests
from db import Mongo


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

    def get_wmsession_id(self, tp):
        filter_data = {"$where": "function() {return this.timestamp>%d}" % tp, "_ac_type": "5"}
        data = self.__db.find_all(sort_way=-1, field="timestamp", filter=filter_data)
        for i in data:
            print(i)


if __name__ == '__main__':
    db = Dclog()
    db.get_wmsession_id(tp=1576671452450)