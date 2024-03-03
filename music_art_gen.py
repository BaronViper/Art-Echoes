from krita import *

def trigger_plugin():
    doc = Krita.instance().createDocument(1000, 1000, "Music_Gen", "RGBA", "U8", "", 120.0)
    Krita.instance().activeWindow().addView(doc)