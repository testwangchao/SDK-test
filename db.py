import pymongo


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

    def get_db(self):
        my_db = self.mongo.get_database(self.db)
        return my_db[self.db]

    def close(self):
        self.mongo.close()


if __name__ == '__main__':
    db = Mongo()
    # db.get_db().drop()
    data = db.get_db().find({
        "_ac_type": "2",
        "category": "init"
    })
    for i in data:
        print(i)