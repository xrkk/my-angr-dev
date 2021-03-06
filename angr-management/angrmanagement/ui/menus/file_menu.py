
from PySide2.QtGui import QKeySequence
from PySide2.QtCore import Qt

from .menu import Menu, MenuEntry, MenuSeparator


class FileMenu(Menu):
    """
    Lays out the entries under the 'File' menu
    """
    def __init__(self, main_window):
        super().__init__("&File", parent=main_window)

        self.entries.extend([
            MenuEntry('L&oad a new binary...', main_window.open_file_button, shortcut=QKeySequence(Qt.CTRL + Qt.Key_O)),
            MenuEntry('Loa&d a new docker target...', main_window.open_docker_button,
                      shortcut=QKeySequence(Qt.SHIFT + (Qt.CTRL + Qt.Key_O))),
            MenuEntry('Load a &trace file...', main_window.open_trace_file_button,
                      shortcut=QKeySequence(Qt.SHIFT + (Qt.CTRL + Qt.Key_T))),
            MenuSeparator(),
            MenuEntry('&Load angr database...', main_window.load_database, shortcut=QKeySequence(Qt.CTRL + Qt.Key_L)),
            MenuEntry('&Save angr database...', main_window.save_database, shortcut=QKeySequence(Qt.CTRL + Qt.Key_S)),
            MenuEntry('S&ave angr database as...', main_window.save_database_as, shortcut=QKeySequence("Ctrl+Shift+S")),
            MenuSeparator(),
            MenuEntry('Load a new &trace...', main_window.load_trace),
            MenuSeparator(),
            MenuEntry('&Preferences...', main_window.preferences, shortcut=QKeySequence(Qt.CTRL + Qt.Key_P)),
            MenuSeparator(),
            MenuEntry('E&xit', main_window.quit),
        ])
