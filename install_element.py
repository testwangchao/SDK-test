from uiautomator2.watcher import Watcher


class WatchInstall:
    __CANCEL = "取消"
    __NEXT = "下一步"
    __INSTALL = "安装"
    __FINISH = "完成"
    __OPEN = "打开"

    def __init__(self, d: "uiautomator2.Device"):
        self._watcher = Watcher(d)
        
    def simulator(self, interval=0.5):
        # click next to install
        next_to_intall = [self.__CANCEL, self.__NEXT]
        self.watcher_click(next_to_intall, "next to install").click()

        # click install
        install = [self.__CANCEL, self.__INSTALL]
        self.watcher_click(install, "install").click()

        self._watcher.start(interval)

    def stop_watch(self):
        self._watcher.stop()

    def watcher_click(self, button_list: list, name: str):
        count = 0
        watchers = self._watcher(name)
        for i in button_list:
            count += 1
            if count == len(button_list):
                watchers.when(i)
                return watchers
            watchers.when(i)

    def samsung(self):
        # 允许安装次来源的未知程序
        accept_install = [self.__CANCEL, self.__INSTALL]
        self.watcher_click(accept_install, "next to install").click()
        self._watcher.when("确认").click()
        self._watcher.start(interval=0.5)