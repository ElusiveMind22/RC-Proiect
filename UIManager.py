import threading
from tkinterx import *
"""
    This class creates the UI
"""


class UIManager(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
