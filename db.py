import pymongo
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
    
    def __db_sort(self, result, sort_way, field):
        if not field:
            raise DbSortFieldIsNone()
        else:
            return result.sort(field, sort_way)
        
    def find_all(self, sort_way=None, field=None, *args, **kwargs):
        if sort_way:
            return self.__db_sort(result=self.get_db.find(*args, **kwargs), sort_way=sort_way, field=field)
        else:
            return self.get_db.find(*args, **kwargs)

    def find_one_data(self, sort_way=None, field=None, *args, **kwargs):
        if sort_way:
            return self.__db_sort(result=self.get_db.find_one(*args, **kwargs), sort_way=sort_way, field=field)
        else:
            return self.get_db.find_one(*args, **kwargs)


if __name__ == '__main__':
    db = Mongo()
    for i in db.find_all(sort_way=-1, field="seq_id", filter={"adtype": "1"}):
        print(i)