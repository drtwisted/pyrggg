
import sys

from lib import get_random_numbers
from main_window import Ui_PyRGGGWindow
from PyQt4 import QtCore, QtGui
from time import sleep

from modules.roller import Roller


class PyRGGG(QtGui.QMainWindow):
    def __init__(self, parent=None, app=None):
        QtGui.QWidget.__init__(self, parent)
        self.GAMES_DIR = 'games'
        self.current_games_list = list()
        self.app = app
        self.ui = Ui_PyRGGGWindow()
        self.ui.setupUi(self)
        self.ui.bRoll.clicked.connect(self.do_roll)

        self.labels = [self.ui.lbFirstGame,
                       self.ui.lbSecondGame,
                       self.ui.lbTheGame,
                       self.ui.lbForthGame,
                       self.ui.lbLastGame]

        self.roller = Roller(self.labels)

        self.connect(self.roller, QtCore.SIGNAL('update(PyQt_PyObject)'),
                     self._update_game_labels)

    def do_roll(self):
        self.ui.bRoll.setEnabled(False)

        self.roller.set_random_list(self._get_display_list())
        self.roller.run()

        while self.roller.isRunning():
            pass

        self.ui.bRoll.setEnabled(True)
        self.ui.centralwidget.repaint()

    def _read_names(self, platform=''):
        """
        :return: (list(), elements count)
        """
        # _len = 1313
        # return [i for i in range(1, _len)]
        with open('./{0}/{1}.dat'.format(self.GAMES_DIR, platform)) as f:
            return f.readlines()

    def _get_display_list(self):
        self.current_games_list = self._read_names('amg')
        return [self.current_games_list[i]
                for i in
                get_random_numbers(len(self.current_games_list), 3000)]

    def _update_game_labels(self, _list):
        # print(_list)

        for i in range(len(self.labels)):
            self.labels[i].setText(_list[i])
            self.labels[i].repaint()
        self.labels[-1].repaint()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    pyrggg = PyRGGG()
    pyrggg.show()
    sys.exit(app.exec_())
