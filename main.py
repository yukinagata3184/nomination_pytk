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
    gui.root.mainloop()

if __name__ == "__main__":
    main()