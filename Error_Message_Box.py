from tkinter import *

font_type = "Helvetica"
red = "#fe3030"
white = "#ffffff"
black = "#000000"
close_button_str = "Close"


class ErrorMessageBox:

    def __init__(self, master, message):
        self._master = master
        self.config_master()
        self.generate_error_label(master, message).pack()
        self.generate_close_button(master).pack()

    def generate_close_button(self, master):
        return Button(master, text=close_button_str, command=master.destroy, font=(font_type, 14), relief=GROOVE, padx=5, pady=5, bd=1, background=red, fg=black)

    def generate_error_label(self, master, message):
        label = Label(master, text=message)
        label.config(font=(font_type, 20), padx=10, pady=10, background=white)
        return label

    def config_master(self):
        self._master.config(background=white, padx=5, pady=5)
