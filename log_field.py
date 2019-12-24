from dclog import Dclog
from tools.utils import parse_log
import exceptions


class FilterPara:
    test_two_point_request = {"_ac_type": "2", "category": "request", "adtype": "1"}


class LogField:

    BASE_FIELD_LIST = [
            "android_id", "battery_level", "battery_save_enabled", "battery_state", "carrier", "cheight", "clientpixel",
            "clienttype", "clientversion", "cwidth", "device_type", "gameversion", "imei", "imei1", "imei2", "isEmulator",
            "lat", "lng", "load_id", "networktype", "os", "pkgname", "screenangle", "screendensity", "sdkversion",
            "seq_id", "uid", "wifi_id", "wifi_mac", "browser", "vlist"
        ]

    def __init__(self, wmsession_id, **kwargs):
        self.wmsession_id = {"wmsession_id": wmsession_id}
        self.__dclog = Dclog()
        self.not_exist_field = kwargs.get("not_exist_field") if kwargs.get("not_exist_field") else None
        self.remove_not_exist_field()

    @property
    def filter_result(self):
        result = parse_log(self.para)
        if len(result) == 1:
            return result[0]
        else:
            raise exceptions.LogDataError

    def remove_not_exist_field(self):
        if self.not_exist_field:
            for i in self.not_exist_field:
                self.BASE_FIELD_LIST.remove(i)

    def __call__(self, attr):
        try:
            para = getattr(FilterPara, attr)
        except AttributeError:
            raise AttributeError("'FilterPara' object has no attribute '%s'" % attr)
        para.update(self.wmsession_id)
        self.para = para 
        return para


if __name__ == '__main__':
    para = {"_ac_type": "2", "category": "request", "adtype": "2"}
    l = LogField(wmsession_id="bb36fd8-1f61-4fa4-8845-2747e3f8cd18", para=para, not_exist_field=["vlist", "load_id"])
    print(l(attr="test_two_point_request"))
    print(l.BASE_FIELD_LIST)
