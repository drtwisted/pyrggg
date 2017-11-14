import sys

from configparser import ConfigParser
from lib import get_random_numbers
from main_window import Ui_PyRGGGWindow
from PyQt4 import QtCore, QtGui
from time import sleep
from webbrowser import open as web_open

from modules.roller import Roller


EP_URL_TEMPLATE = (
    "http://www.emuparadise.me/roms/search.php?query={0}&section=all")


# Main Window Class
class PyRGGG(QtGui.QMainWindow):
    def __init__(self, parent=None, app=None):
        QtGui.QWidget.__init__(self, parent)
        self.PLATFORMS_DIR = 'platforms'
        self.IMAGES_DIR = 'images'
        self.ICONS_DIR = '{0}/icons/'.format(self.IMAGES_DIR)

        self._the_game_press_event_backup = None
        self._config = ConfigParser()
        self._config.read('platforms.ini')

        self.current_games_list = list()
        self.app = app
        self.ui = Ui_PyRGGGWindow()
        self.ui.setupUi(self)

	# Signals connections
        self.ui.bRoll.clicked.connect(self.do_roll)

        self.labels = [self.ui.lbFirstGame,
                       self.ui.lbSecondGame,
                       self.ui.lbTheGame,
                       self.ui.lbForthGame,
                       self.ui.lbLastGame]

        self.platforms = self._config['platforms']
        self.platforms_icons = dict()
        self.current_platform = ''
        self.current_game_pix_map = None
        self.__populate_platforms()
        self.__load_graphics()

        self.roller = Roller(self.labels)

        self.connect(self.roller, QtCore.SIGNAL('update(PyQt_PyObject)'),
                     self._update_game_labels)

        self.ui.cbPlatforms.activated.connect(
            self._combobox_select)

        self._select_first_platform()

    def _select_first_platform(self):
        self._combobox_select()

    def __add_icon_to_platform_name(self):
        icon = self.platforms_icons[self.current_platform]
        self.ui.lbCurrPlatformIcon.setPixmap(icon.pixmap(QtCore.QSize(64, 64)))

    def __populate_platforms(self):
        # Set first element on the list
        self.current_platform = self.platforms._options()[0]

        for p in self.platforms:
            self.platforms_icons[p] = QtGui.QIcon(
                '{0}{1}.png'.format(self.ICONS_DIR, p))
            self.ui.cbPlatforms.addItem(self.platforms_icons[p],
                                        self.platforms[p])

    def __load_graphics(self):
        # Load Icon from file and get it's 32x32 pix map
        self.current_game_pix_map = QtGui.QIcon(
            '{0}curr_game.png'.format(self.ICONS_DIR)).pixmap(
            QtCore.QSize(32, 32))

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
        self.set_url_clicker(False)
        self.set_current_game_icon_active(False)
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

    def the_game_clicked(self, event):
        game_name = self.ui.lbTheGame.text()
        web_open(EP_URL_TEMPLATE.format("{0} {1}".format(
            game_name, self.current_platform)))

    def set_url_clicker(self, state):
        if state:
            self.ui.lbTheGame.mousePressEvent = self.the_game_clicked
        else:
            # Dirty hack to replace with dummy event
            self.ui.lbTheGame.mousePressEvent = lambda obj, p_obj, event: None

    def set_controls_enabled(self, state):
        self.set_url_clicker(state)
        self.ui.bRoll.setEnabled(state)
        self.ui.cbPlatforms.setEnabled(state)

    def set_current_game_icon_active(self, active=True):

        if active:
            pix_map = self.current_game_pix_map
            max_width = 32
        else:
            pix_map = QtGui.QPixmap()
            max_width = 0
        
        for lbIcon in [self.ui.lbTheGameIconLeft, self.ui.lbTheGameIconRight]:
            lbIcon.setMinimumWidth(max_width)
            lbIcon.setMaximumWidth(max_width)
            lbIcon.setFixedWidth(max_width)
            lbIcon.setPixmap(pix_map)

    def do_roll(self):
        if self.current_platform and self.current_platform != '':
            self.set_controls_enabled(False)
            self.set_current_game_icon_active(False)

            self.roller.set_random_list(self._get_display_list())
            self.roller.run()

            while self.roller.isRunning():
                self.app.processEvents()

            self.set_current_game_icon_active()
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
            return [l.strip('\n') for l in f.readlines()]
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
