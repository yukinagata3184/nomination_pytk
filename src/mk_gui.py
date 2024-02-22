##
# @file mk_gui.py
# @brief This file implements creation of the GUI canvas, 
# @brief placement of images and buttons, and actions when buttons are clicked.
# @author yukinagata3184

import tkinter
import random

class MkGUI:
    """! Make GUI class.
    """
    def __init__(self):
        """! Make tkinter.Tk() instance.
        """
        self.root = tkinter.Tk()

    def mk_canvas(self, title="app name", is_resize=False, width=1000, height=600):
        """! Create a canvas for the GUI.
        @param title [str] Title of app.
        @param is_resize [bool] Specifies whether the window can be resized.
        @param width [int] Window width.
        @param height [int] Window height.
        """
        self.root.title(title)
        self.root.resizable(is_resize, is_resize)
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()