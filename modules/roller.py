from math import sqrt, tan, pow
from PyQt4.QtCore import QThread, SIGNAL
from time import sleep


class Roller(QThread):
    def __init__(self, labels=None, random_list=None):
        super(QThread, self).__init__()
        self._labels = labels
        self._list = None
        self.set_random_list(random_list)

    def set_random_list(self, _list):
        self._list = _list

    def run(self):
        _list = self._list
        labels_count = len(self._labels)
        list_len = len(_list)
        for i in range(0, list_len, 5):

            # sleep
            const_percent = (list_len / 100) * 63.5
            modifier = abs(tan(i / const_percent))
            sleep(0.01 * modifier)

            res_list = list()
            for j in range(labels_count - 1):
                res_list.append(self._labels[j + 1].text())
                # self._labels[j].setText()
            res_list.append(_list[i])

            self.emit(SIGNAL('update(PyQt_PyObject)'), res_list)

