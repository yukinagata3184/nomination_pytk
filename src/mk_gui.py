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
    def __init__(self, title="app name", is_resize=False, width=1000, height=600):
        """! Create a canvas for the GUI.
        @param title [str] Title of app.
        @param is_resize [bool] Specifies whether the window can be resized.
        @param width [int] Window width.
        @param height [int] Window height.
        """
        self.root = tkinter.Tk()
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

    def place_label(self, text="？？？", font="Times New Roman", font_size=70,
                        bg_color="white", x_axis=300, y_axis=75):
        """! Place the text on the canvas.
        @param text [str] Text to be displayed on the label.
        @param font [str] Font of the text to be displayed on the label.
        @param font_size [int] Font size of the text to be displayed on the label.
        @param bg_color [str] Background color of the text to be displayed on the label.
        @param x_axis [int] x-axis of the label.
        @param y_axis [int] y-axis of the label.
        """
        self.label = tkinter.Label(self.root, text=text, font=(font, font_size), bg=bg_color)
        self.label.place(x=x_axis, y=y_axis)

    def place_button(self, text="Button", font="Times New Roman", font_size=36,
                     text_color="blue", x_axis=300, y_axis=230,
                     action_button_click=None):
        """! Place the button on the canvas.
        @param text [str] Text to be displayed on the button.
        @param font [str] The font of the text to be displayed on the button.
        @param font_size [int] The font size of the text to be displayed on the button.
        @param text_color [str] The text color on the button.
        @param x_axis [int] x-axis of the button.
        @param y_axis [int] y-axis of the button.
        @param action_button_click [func] Action when button clicked.
        """
        button = tkinter.Button(self.root, text=text, font=(font, font_size), fg=text_color,
                                command=action_button_click)
        button.place(x=x_axis, y=y_axis)

    def get_list(self, get_list=[]):
        """! Get list in instance variable for use other methods.
        @param get_list [list] Get list in instance variable.
        """
        self.get_list = get_list
        self.selected_get_list = []

    def action_nominate_button_click(self, finish_txt="終了",
                                     front_honorific="", after_honorific="さん"):
        """! Nominate when the button is clicked.
        @param finish_txt [str] The text to be displayed after finished nominating everyone.
        @param front_honorific [str] The honorific title front of name.
        @param after_honorific [str] The honorific title after of name.
        """
        element_num = len(self.get_list)
        if element_num == 0:
            self.label["text"] = finish_txt
        else:
            element_choice = random.choice(list(range(0, element_num, 1)))
            popped_name = self.get_list.pop(element_choice)
            self.label["text"] = front_honorific + popped_name + after_honorific
            self.selected_get_list.append(popped_name)
        self.label.update()

    def action_reset_button_click(self, text_after_reset="？？？"):
        """! Reset when the button is clicked.
        @param text_after_reset The text to display after clicking the reset button.
        """
        for i in self.selected_get_list:
            self.get_list.append(i)
        self.selected_get_list = []
        self.label["text"] = text_after_reset