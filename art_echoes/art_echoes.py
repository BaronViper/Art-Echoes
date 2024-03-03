from krita import *
from .music_gen import *
from .brush_events import exec_win


def start_win():
    doc = Krita.instance().createDocument(1000, 1000, "Music_Gen", "RGBA", "U8", "", 120.0)
    Krita.instance().activeWindow().addView(doc)

    # song_gen([[(0,0), (1,2)]])  # dummy data
    # win = InputInfo()
    # win.show()
    exec_win(Krita.instance().activeWindow())

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
