import json
import requests
import exceptions
from lxml import etree
from urllib.parse import unquote
import copy


class Dclog:

    BASE_FIELD_LIST = [
        "android_id", "battery_level", "battery_save_enabled", "battery_state", "carrier", "cheight", "clientpixel",
        "clienttype", "clientversion", "cwidth", "device_type", "gameversion", "imei", "imei1", "imei2", "isEmulator",
        "lat", "lng", "load_id", "networktype", "os", "pkgname", "screenangle", "screendensity", "sdkversion",
        "seq_id", "uid", "wifi_id", "wifi_mac", "browser", "vlist", "timestamp"
    ]
    __UNIQ_KEY = "sigandroid_1328"

    TEST_TWO_POINT_REQUEST = {"_ac_type": "2", "category": "request", "adtype": "2"}

    def __init__(self, wmsession_id,  paras=None):
        self.filter_para = {"wmsession_id": wmsession_id, "_uniq_key": self.__UNIQ_KEY}
        # for k in kwargs:
        #     self.filter_para[k] = kwargs.get(k)
        self.paras = paras
        if self.paras:
            self.filter_para.update(self.paras)

    def __setitem__(self, key, value):
        self.filter_para[key] = value

    def __delitem__(self, key):
        del self.filter_para[key]

    def parse_log(self, para):

        '''
        :param para: dict()
        egg: {"_uniq_key":"sigandroid_1328","_ac_type":"5","category":"request","wmsession_id":"37c18265-1364-4ff1-81e3-90bdc0e837d4","adtype":"1"}
        :return: search result
        '''
        url = "".format(json.dumps(para))
        resp = requests.get(url=url).text
        dom = etree.HTML(resp)
        table_len = len(dom.xpath("//table"))
        # 打点条数
        table_xpath_list = []
        for i in range(1, table_len + 1):
            table_xpath_list.append("//table[{0}]".format(i))
        # 打点字段
        all_data = []
        for field_data in table_xpath_list:
            field_table = field_data + "//tr[1]/th"
            value_data = field_data + "//tr[2]/td[{0}]"
            field_value = {}
            # 解析每条打点log中的字段和对应的值
            for index, result_field in enumerate(dom.xpath(field_table), 1):
                if result_field.text in ["_time_stamp", "_uniq_key", "ip", "request_ip", "server_name"]:
                    continue
                field_dom = dom.xpath(value_data.format(index))[0].text
                try:
                    field_value[result_field.text] = unquote(field_dom)
                except TypeError:
                    field_value[result_field.text] = field_dom
            all_data.append(field_value)

        return all_data

    def clear_para(self):
        for k in list(self.filter_para):
            if k in ["wmsession_id", "_uniq_key"]:
                continue
            del self.filter_para[k]

    def remove_field(self, remove_lt=None, need_list=None):
        data = copy.deepcopy(self.BASE_FIELD_LIST)
        for remove_key in remove_lt:
            data.remove(remove_key)
        if need_list:
            for need_key in need_list:
                data.append(need_key)
        return data


if __name__ == '__main__':
    dclog = Dclog(wmsession_id="7c8e0a68-3b0b-4a53-9c78-ca2834df45f5")
    paras = [{"two_point_request": {"_ac_type": "2", "category": "request", "adtype": "1"}, "remove_lt": ["vlist", "load_id"]}]
    for para in paras:
        for k in para:
            value = para.get(k)
            if isinstance(value, dict):
                for key in value:
                    dclog[key] = value.get(key)
        data = dclog.remove_field(remove_lt=para.get("remove_lt", None), need_list=para.get("need_list", None))
        print(dclog.filter_para)
        dclog.clear_para()
        print(dclog.filter_para)
        print(data)
