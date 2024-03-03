from .music_gen import song_gen

from krita import Krita

from PyQt5.QtCore import (
    Qt,
    QCoreApplication
)

from PyQt5.QtGui import (
    QMouseEvent,
    QTabletEvent,
    QTextCursor
)

from PyQt5.QtWidgets import (
    QPlainTextEdit,
    QWidget, QMessageBox, QApplication, QDialog, QHBoxLayout, QPushButton
)

total_coords = []

# Find the current Krita canvas; function taken from
# https://krita-artists.org/t/clicking-with-scripts/26150/5
# by AkiR
def find_current_canvas():
    app = Krita.instance()
    try:
        q_window = app.activeWindow().qwindow()
        q_stacked_widget = q_window.centralWidget()
        q_mdi_area = q_stacked_widget.currentWidget()
        q_mdi_sub_window = q_mdi_area.currentSubWindow()
        view = q_mdi_sub_window.widget()
        for c in view.children():
            if c.metaObject().className() == 'KisCanvasController':
                # first QWidget child of viewport should be canvas...
                viewport = c.viewport()
                canvas = viewport.findChild(QWidget)
                return canvas
    except:
        return None


# Debugging info function taken from
# https://krita-artists.org/t/to-monitor-the-cursor-position/75694/4
# by AkiR
def flag_to_human(flag, enum_cls, owner):
    pairs = list()
    for name in dir(owner):
        value = getattr(owner, name)
        if isinstance(value, enum_cls) and value > 0:
            pairs.append((value, name))
    pairs.sort(reverse=True)
    flag_value = int(flag)
    flag_list = list()
    for v, name in pairs:
        if flag_value >= int(v):
            flag_list.append(name)
            flag_value -= v
    return flag_list


# Use this window to show debugging info about left mouse events
# Function adapted from
# https://krita-artists.org/t/to-monitor-the-cursor-position/75694/4
# by AkiR
class InputInfo(QPlainTextEdit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hook_core_app()


    def closeEvent(self, event):
        self.release_core_app()
        return super().closeEvent(event)

    def hook_core_app(self):
        """ add hook to core application. """
        q_app = QCoreApplication.instance()
        q_app.installEventFilter(self)

    def release_core_app(self):
        """ remove hook from core application. """
        # do these things when the window is closed
        if total_coords: song_gen([total_coords])
        q_app = QCoreApplication.instance()
        q_app.removeEventFilter(self)

    def eventFilter(self, obj, event):
        if isinstance(event, (QMouseEvent, QTabletEvent)):
            canvas = find_current_canvas()
            # let's do something smart!
            # Like sort big enum lists and print some text,
            # everytime mouse moves one pixel...
            modifiers = flag_to_human(event.modifiers(), Qt.KeyboardModifier, Qt)
            buttons = flag_to_human(event.buttons(), Qt.MouseButton, Qt)
            # Modification: Only do for left button down event and if
            # Krita canvas is the active canvas
            if 'LeftButton' in buttons and canvas and canvas.isActiveWindow():
                # Add current coordinates to list
                total_coords.append((event.x(),event.y()))
                # self.append_to_end(
                #         f'pos = {event.pos()}\n'
                #         f'modifiers = {modifiers}\n'
                #         f'buttons = {buttons}\n'
                #         f'mylist = {total_coords}\n')
        return super().eventFilter(obj, event)

    # def append_to_end(self, text):
    #     self.moveCursor(QTextCursor.End)
    #     self.insertPlainText(text)

# def exec_win(activeWin):
    # canvas = find_current_canvas()
    # layoutForButtons = QHBoxLayout()
    # newButton = QPushButton("Press me")
    # layoutForButtons.addWidget(newButton)

win = InputInfo()
    # win.setParent(canvas)
    # win.setLayout(layoutForButtons)
    # win.setWindowTitle("test")
    # win.setVisible(True)
win.show()
