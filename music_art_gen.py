from krita import *

def trigger_my_plugin():
    Krita.instance().action("music-art-gen").trigger()