

class BaseException(Exception):
    pass


class DbSortFieldIsNone(BaseException):
    pass


class AdLoadFailed(BaseException):
    def __init__(self, msg):
        self.msg = msg
        
        
if __name__ == '__main__':
    if 1:
        raise AdLoadFailed("test")