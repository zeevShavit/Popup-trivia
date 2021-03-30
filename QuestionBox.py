from tkinter import *


font_type = "Helvetica"
green = "#01ce65"
red = "#fe3030"
category_color = "#16b6de"
white = "#ffffff"
black = "#000000"
close_button_str = "Close"
correct_str = "Correct!"
wrong_str = "Wrong!"
category_str = "Category: "
correct_answer_str = "The correct answer is: "
bold = "bold"


class AnswerButton:

    def __init__(self, answer, index, frame, callback):
        self._frame = frame
        self._index = index
        self._answer_button = Button(frame, text=answer.get_answer_str(), command=lambda: callback(index), relief=GROOVE, padx=10, pady=10)
        self._answer_button.config(font=(font_type, 14), bg=green, border=1, fg=black)

    def get_instance(self):
        return self._answer_button


class QuestionBox:

    def __init__(self, master, question):
        self._question = question
        self._master = master
        self.config_master()
        self.generate_category().pack()
        self.generate_question().pack()
        self.generate_answers_buttons().pack()
        self.generate_close_button().pack()

    def generate_answers_buttons(self):
        frame_buttons = Frame(self._master, relief=RIDGE, padx=10, pady=10, background=white)
        line_max_len = 20
        longest_answer = self.find_longest_answer_len()
        self.fill_frame_with_answer_buttons(frame_buttons, line_max_len, longest_answer)
        return frame_buttons

    def fill_frame_with_answer_buttons(self, frame, line_max_len, longest_answer):
        for index, answer in enumerate(self._question.get_answers_list()):
            answer_button = self.generate_single_answer_button(frame, answer, index, line_max_len, longest_answer)
            self.place_answer_button_in_frame(answer_button, index)

    def place_answer_button_in_frame(self, answer_button, index):
        answer_button.grid(row=index - index % 2, column=index % 2, padx=1, pady=1)

    def generate_single_answer_button(self, frame, answer, index, line_max_len, longest_answer):
        answer_button = AnswerButton(answer, index, frame, self.is_correct_msg).get_instance()
        answer_button.config(height=10, width=max(longest_answer, line_max_len))
        return answer_button

    def find_longest_answer_len(self):
        longest_answer = 0
        for answer in self._question.get_answers_list():
            longest_answer = max(len(answer.get_answer_str()), longest_answer)
        return longest_answer

    def generate_question(self):
        label = Label(self._master, text=self._question.get_question_str(), wraplength=800)
        label.config(font=(font_type, 20), padx=10, pady=10, background=white)
        return label

    def generate_category(self):
        label = Label(self._master, text=category_str + str(self._question.get_category()))
        label.config(font=(font_type, 14), padx=10, pady=10, fg=category_color, bd=1, background=white)
        return label

    def config_master(self):
        self._master.config(background=white, padx=5, pady=5)

    def generate_correct_label(self):
        label = Label(self._master, text=correct_str)
        label.config(font=(font_type, 40, bold), foreground=green, padx=10, pady=10, background=white)
        return label

    def generate_wrong_message_label(self):
        label = Label(self._master, text=wrong_str, foreground=red, padx=10, pady=10)
        label.config(font=(font_type, 40, bold), background=white)
        return label

    def generate_correct_answer_label(self):
        label = Label(self._master, text=correct_answer_str + self._question.get_correct_answer_str())
        label.config(font=(font_type, 12), background=white, padx=10, pady=10)
        return label

    def is_correct_msg(self, index):
        self.clear_all_widgets()
        self.fill_correct_msg_window(index)
        self.generate_close_button().pack()

    def fill_correct_msg_window(self, index):
        if self._question.is_correct_answer(index):
            self.generate_correct_label().pack()
        else:
            self.generate_wrong_message_label().pack()
            self.generate_correct_answer_label().pack()

    def clear_all_widgets(self):
        for widget in self._master.winfo_children():
            widget.destroy()

    def generate_close_button(self):
        close_button = Button(self._master, text=close_button_str, command=self._master.destroy, font=(font_type, 14), relief=GROOVE, bd=1, background=red, fg=black)
        return close_button
