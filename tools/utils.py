import json
import time

import requests
from lxml import etree
from urllib.parse import unquote


def get_current_time_stamp(c_time):
    current_time_stamp = int(round(c_time * 1000))
    return current_time_stamp


def parse_log(para):
    '''
    :param para: dict()
    egg: {"_uniq_key":"sigandroid_1328","_ac_type":"5","category":"request","wmsession_id":"37c18265-1364-4ff1-81e3-90bdc0e837d4","adtype":"1"}
    :return:
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
            # 判断字段对应的值是否为空
            if dom.xpath(value_data.format(index))[0].text:
                field_value[result_field.text] = unquote(dom.xpath(value_data.format(index))[0].text)
            else:
                field_value[result_field.text] = dom.xpath(value_data.format(index))[0].text
            # 解码URL链接
            # if re.search(".*url.*", result_field.text):
            #     field_value[result_field.text] = unquote(dom.xpath(value_data.format(index))[0].text)
            #     continue
            # field_value[result_field.text] = dom.xpath(value_data.format(index))[0].text

        # 将server log中的price_的值替换为price_raw的值，SDK原始值为price_raw的值
        if "price" in field_value.keys():
            if "price_raw" in field_value.keys():
                field_value["price"] = field_value["price_raw"]
                field_value.pop("price_raw")
        # if "content-type" in field_value.keys():
        #     field_value["content-type"] = unquote(field_value["content-type"])
        if "battery_level" in field_value.keys():
            field_value["battery_level"] = field_value["battery_level"]
        all_data.append(field_value)

    return all_data


if __name__ == '__main__':
    print(get_current_time_stamp(time.time()))