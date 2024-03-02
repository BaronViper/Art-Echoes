from krita import *
from music_gen import *

def trigger_my_plugin():
    Krita.instance().action("music_art_gen").trigger()