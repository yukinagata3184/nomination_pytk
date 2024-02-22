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
    
    def place_img(self, img_path="img/teacher_india_man.png", x_axis=150, y_axis=250):
        """! Place the image on the canvas.
        @param img_path [str] The path to the image to be displayed.
        @param x-axis [int] x-axis of the image.
        @param y-axis [int] y-axis of the image.
        """
        self.img = tkinter.PhotoImage(file=img_path)
        self.canvas.create_image(x_axis, y_axis, image=self.img)
