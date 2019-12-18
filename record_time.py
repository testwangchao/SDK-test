import time


class RecordTime:

    def __init__(self):
        self.current_time = {}

    def __call__(self, **kwargs):
        self.current_time.update(kwargs)


if __name__ == '__main__':
    rt = RecordTime()
    t = int(round(time.time() * 1000))
    rt(ct = t)
    time.sleep(5)
    rt(ct2 = int(round(time.time() * 1000)))
    print(rt.current_time)