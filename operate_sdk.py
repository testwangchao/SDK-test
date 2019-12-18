from driver import InitDriver


class OperateSdk:
    def __init__(self, driver):
        self.driver = driver

    def click(self, **kwargs):
        a = lambda x:list(x.keys)
        a(kwargs)[0] = kwargs.get(a(kwargs)[0])


if __name__ == '__main__':
    def func(**kwargs):
        a = lambda x: list(x.keys())
        a(kwargs)[0] = kwargs.get(a(kwargs)[0])
        print(a(kwargs)[0])
    func(v = 1)

    


