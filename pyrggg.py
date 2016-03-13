
import sys

from configparser import ConfigParser
from lib import get_random_numbers
from main_window import Ui_PyRGGGWindow
from PyQt4 import QtCore, QtGui
from time import sleep

from modules.roller import Roller


class PyRGGG(QtGui.QMainWindow):
    def __init__(self, parent=None, app=None):
        QtGui.QWidget.__init__(self, parent)
        self.PLATFORMS_DIR = 'platforms'
        self.IMAGES_DIR = 'images'
        self.ICONS_DIR = '{0}/icons/'.format(self.IMAGES_DIR)

        self._config = ConfigParser()
        self._config.read('platforms.ini')

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

        self.platforms = self._config['platforms']
        self.platforms_icons = dict()
        self.current_platform = ''
        self.__populate_platforms()

        # self.platforms = [self.ui.btnPlatformNes,
        #                   self.ui.btnPlatformAmiga,
        #                   self.ui.btnPlatformSMD,
        #                   self.ui.btnPlatformSNES]
        # self.gbPlatforms = QtGui.QButtonGroup()
        # for p in self.platforms:
        #     self.gbPlatforms.addButton(p)
        #     p.clicked.connect(self.__on_platform_button_click)

        self.roller = Roller(self.labels)

        self.connect(self.roller, QtCore.SIGNAL('update(PyQt_PyObject)'),
                     self._update_game_labels)

        # for i in range(5):
        #     self.ui.cbPlatforms.addItem(str(i + 1), i + 1)

        self.ui.cbPlatforms.activated.connect(
            self._combobox_select)

        self._select_first_platform()

    def _select_first_platform(self):
        self._combobox_select()

    def __add_icon_to_platform_name(self):
        icon = self.platforms_icons[self.current_platform]
        self.ui.lbCurPlatformIcon.setPixmap(icon.pixmap(QtCore.QSize(32, 32)))

    def __populate_platforms(self):
        # Set first element on the list
        self.current_platform = self.platforms._options()[0]

        for p in self.platforms:
            self.platforms_icons[p] = QtGui.QIcon(
                '{0}{1}.png'.format(self.ICONS_DIR, p))
            self.ui.cbPlatforms.addItem(self.platforms_icons[p],
                                        self.platforms[p])

    def _get_platform_id_by_name(self, name):
        for p in self.platforms:
            if self.platforms[p] == name:
                return p

    def _combobox_select(self, *args, **kwargs):
        self.current_platform = self._get_platform_id_by_name(
            self.ui.cbPlatforms.currentText())
        self._clear_roller()

        self._update_games_list()
        self.ui.lbTotlaGames.setText('Games in DB: {0}'.format(str(
            len(self.current_games_list))))

        self.ui.lbCurPlatform.setText(
            'Current platform: {0}'.format(
                self.platforms[self.current_platform]))
        self.__add_icon_to_platform_name()
        # print(
        #     'Selected: ' + self.ui.cbPlatforms.currentText() + '; ind = ' +
        #       str(self.ui.cbPlatforms.currentIndex()))

    def _clear_roller(self):
        for l in self.labels:
            l.setText('------')

    def __on_platform_button_click(self):
        self.current_platform = self.gbPlatforms.checkedButton().text().lower()
        self._clear_roller()
        # if isinstance(args[0], QtGui.QPushButton):
        #     print("it's a button!")
        # else:
        #     print("nosssing!")

    def set_controls_enabled(self, state):
        self.ui.bRoll.setEnabled(state)
        self.ui.cbPlatforms.setEnabled(state)

    def do_roll(self):
        if self.current_platform and self.current_platform != '':
            self.set_controls_enabled(False)

            self.roller.set_random_list(self._get_display_list())
            self.roller.run()

            while self.roller.isRunning():
                self.app.processEvents()

            self.set_controls_enabled(True)
            self.ui.centralwidget.repaint()

    def _read_names(self, platform=''):
        """
        :return: (list(), elements count)
        """
        # _len = 1313
        # return [i for i in range(1, _len)]
        # try:
        with open('./{0}/{1}.dat'.format(
                self.PLATFORMS_DIR, platform)) as f:
            return f.readlines()
        # except Exception as error:
        #     print('Caught Exception: {0}'.format(error))
        #     return []

    def _update_games_list(self):
        self.current_games_list = self._read_names(self.current_platform)

    def _get_display_list(self):
        self._update_games_list()
        return [self.current_games_list[i]
                for i in
                get_random_numbers(len(self.current_games_list), 3000)]

    def _update_game_labels(self, _list):
        # print(_list)

        for i in range(len(self.labels)):
            self.labels[i].setText(_list[i])
            self.labels[i].setAlignment(
                QtCore.Qt.AlignCenter)
            self.labels[i].repaint()
        self.labels[-1].repaint()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    pyrggg = PyRGGG()
    pyrggg.show()
    sys.exit(app.exec_())
