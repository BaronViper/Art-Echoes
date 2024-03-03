from krita import *
from .music_gen import *
from .brush_events import InputInfo
from PyQt5.QtWidgets import QWidget, QMessageBox


def start_win():
    doc = Krita.instance().createDocument(1000, 1000, "Music_Gen", "RGBA", "U8", "", 120.0)
    Krita.instance().activeWindow().addView(doc)

    QMessageBox.information(QWidget(), "Art Echoes", "Welcome to Art Echoes, a plug-in to convert drawings to audio. Simply start by drawing on the canvas provided!")
    #
    # win = InputInfo()
    # win.hook_core_app()
    # win.show()


class ArtEchoes(Extension):

    def __init__(self, parent):
        # This is initialising the parent, always important when subclassing.
        super(ArtEchoes, self).__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("art_echoes_id", "Art Echoes", "tools/scripts")
        action.triggered.connect(start_win)

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(ArtEchoes(Krita.instance()))
