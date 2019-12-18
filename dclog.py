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
        data = self.__db.get_db().find(
            {"$where": "function() {return this.timestamp>%d}" % tp}
        ).sort("seq_id", -1)


if __name__ == '__main__':
    db = Dclog()
    print(db.get_wmsession_id(tp=1576671415783))