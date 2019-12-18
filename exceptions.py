

class BaseException(Exception):
    pass


class DbSortFieldIsNone(BaseException):
    pass


class AdLoadFailed(BaseException):
    pass