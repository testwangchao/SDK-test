import json
import time

import requests
from lxml import etree
from urllib.parse import unquote


def get_current_time_stamp(c_time):
    current_time_stamp = int(round(c_time * 1000))
    return current_time_stamp


all_paras = [
    {"two_point_request": {"_ac_type": "2", "category": "request", "adtype": "1"}, "remove_lt": ["vlist", "load_id"], "need_list": []},
    {"two_point_respond": {"_ac_type": "2", "category": "respond", "adtype": "1"}, "remove_lt": [], "need_list": []},
    {"five_point_request": {"_ac_type": "5", "category": "request", "adtype": "1"}, "remove_lt": ["vlist", "load_id"], "need_list":  ["sub_category", "platform"]},
    {"five_point_respond": {"_ac_type": "5", "category": "respond", "adtype": "1"}, "remove_lt": ["vlist", "load_id"], "need_list":  ["campaign_id", "platform", "target_url", "request_id", "sub_category", "ad_source_channel", "price", "creative_id"]}
]


