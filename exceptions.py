

class BaseException(Exception):
    def __init__(self, msg=None):
        self.msg = msg


class DbSortFieldIsNone(BaseException):
    pass


class AdLoadFailed(BaseException):
    pass


class LogDataError(BaseException):
    pass


if __name__ == '__main__':
    if 1:
        raise AdLoadFailed("test")