##
# @file main.py
# @brief This file that impliments the main function of the nomination application.
# @author yukinagata3184

from src.mk_gui import MkGUI

def main():
    """! main function of the nomination app.
    Running this file will run the nomination app.
    """
    gui = MkGUI(title="nomination", is_resize=False, width=1000, height=600)
    gui.place_img(img_path="img/teacher_india_man.png", x_axis=150, y_axis=250)
    gui.place_label(text="選ばれたのは", font="Times New Roman", font_size=40,
                    bg_color="#f0f0f0", x_axis=300, y_axis=0)
    gui.place_label(text="？？？", font="Times New Roman", font_size=70,
                        bg_color="white", x_axis=300, y_axis=75)
    gui.root.mainloop()

if __name__ == "__main__":
    main()