from lib import get_rand
from math import sqrt, tan, pow
from PyQt4.QtCore import QThread, SIGNAL
from time import sleep


class FiveList(list):
    _size_limiter = 5

    def append(self, p_object):
        if self.__len__() == self._size_limiter:
            self.pop(0)

        super(FiveList, self).append(p_object)


class Roller(QThread):
    def __init__(self, labels=None, random_list=None):
        super(QThread, self).__init__()
        self.__previous_list = FiveList()
        self._labels = labels
        self.set_random_list(random_list)
        self._list = None

    def set_random_list(self, _list):
        self._list = _list

    def __update_lables(self, new_value, forward=True):
        res_list = list()

        if forward:
            self.__previous_list.append(self._labels[0].text())
            for i in range(len(self._labels) - 1):
                res_list.append(self._labels[i + 1].text())
            res_list.append(new_value)
        else:
            res_list.append(new_value)
            for i in range(len(self._labels) - 1):
                res_list.append(self._labels[i].text())

        return res_list

    def __send_update_signal(self, _list):
        self.emit(SIGNAL('update(PyQt_PyObject)'), _list)

    def run(self):
        base_sleep_time = 0.005
        _list = self._list
        labels_count = len(self._labels)
        list_len = len(_list)
        for i in range(0, list_len, 5):

            # sleep
            const_percent = (list_len / 100) * 63.5
            modifier = abs(tan(i / const_percent))
            sleep(base_sleep_time * modifier)

            res_list = self.__update_lables(_list[i])

            self.__send_update_signal(res_list)
            # self.__previous_list = list(res_list)

        random_factor = 500
        random_value = get_rand(random_factor, low_margin=200)
        # random_value = get_rand(random_factor)

        # print('random_value: {0}'.format(random_value))

        if random_value > (random_factor / 2):
            devider = 50
            prev_list_len = len(self.__previous_list)
            random_diff = random_factor - random_value
            range_margin = int(random_diff / devider)
            range_margin = (range_margin
                            if range_margin <= prev_list_len
                            else prev_list_len)
            for i in range(1, range_margin):
                sleep(base_sleep_time * devider)
                res_list = self.__update_lables(
                        self.__previous_list[prev_list_len - i], forward=False)
                self.__send_update_signal(res_list)