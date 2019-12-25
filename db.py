import pymongo

import exceptions
from exceptions import DbSortFieldIsNone


class SingletonMode:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonMode, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @staticmethod
    def get_mdb():
        return Mongo().get_db()


class Mongo(SingletonMode):

    def __init__(self, host="localhost", port=27017, db="sigmob"):
        self.db = db
        self.mongo = pymongo.MongoClient(host=host, port=port)
        db_list = self.mongo.list_database_names()
        self.mongo[db] if db not in db_list else print("")

    @property
    def get_db(self):
        my_db = self.mongo.get_database(self.db)
        return my_db[self.db]

    def close(self):
        self.mongo.close()

    def clear_db(self):
        self.get_db.drop()

    def __db_sort(self, result, sort_way, field):
            return result.sort([(field, sort_way)])
        
    def find_all(self, sort_way=None, field=None, *args, **kwargs):
        if sort_way:
            if field:
                return self.__db_sort(result=self.get_db.find(*args, **kwargs), sort_way=sort_way, field=field)
            else:
                raise DbSortFieldIsNone()

        else:
            return self.get_db.find(*args, **kwargs)

    def find_one_data(self, sort_way=None, field=None, *args, **kwargs):
        if sort_way:
            return self.__db_sort(result=self.get_db.find_one(*args, **kwargs), sort_way=sort_way, field=field)
        else:
            return self.get_db.find_one(*args, **kwargs)

    def use_tp_get_need_log(self, record_time):
        '''
        以record_time为分界，过滤打点
        :param record_time: 指定的时间
        :return: dict
        '''
        # 等于使用 ==
        filter_data = {"_ac_type": "2", "category": "request", "adtype": "2"}
        filter_data.update({"$where": "function() {return this.timestamp>%s}" % record_time})
        data = self.find_all(sort_way=-1, field="timestamp", filter=filter_data)
        if data.count() == 1:
            return data[0]
        else:
            return exceptions.LogDataError("查询出的打点数据异常，数量为：%s" % data.count())


if __name__ == '__main__':
    db = Mongo()
    # db.get_db.drop()
    result = db.use_tp_get_need_log(record_time=1577266209170)
    print(result.get("wmsession_id"))