import requests
import time
import random
from Question import Question
from Answer import Answer
from QuestionBox import QuestionBox
from tkinter import *
from Error_Message_Box import ErrorMessageBox
from base64 import b64decode


def get_questions_from_api(questions_amount):
    response = requests.get("https://opentdb.com/api.php?amount=" + str(questions_amount) + "&encode=base64")
    return response.json()


def generate_answers_list(json_data):
    answers_list = [Answer(b64decode(json_data['correct_answer']), True)]
    for answer_str in json_data['incorrect_answers']:
        answers_list.append(Answer(b64decode(answer_str), False))
    return answers_list


def generate_single_question():
    response_json = get_questions_from_api(1)['results'][0]
    answers_list = generate_answers_list(response_json)
    return Question(b64decode(response_json['question']), b64decode(response_json['category']), answers_list)


def raise_window_above_all(window):
    window.lift()
    window.attributes('-topmost', True)


def set_window_position(window):
    position_right = 400
    position_down = 200
    window.geometry("+%d+%d" % (position_right, position_down))


def place_window(window):
    raise_window_above_all(window)
    set_window_position(window)


def set_window_title_bar(window):
    window.title('Popup_Trivia')
    window.iconbitmap('question.ico')


def pop_error_window():
    root = Tk()
    set_window_title_bar(root)
    ErrorMessageBox(root, error_message_str)
    place_window(root)
    raise_window_above_all(root)
    root.mainloop()


def pop_question_window():
    root = Tk()
    QuestionBox(root, question)
    set_window_title_bar(root)
    place_window(root)
    root.mainloop()


if __name__ == '__main__':
    min_time_to_wait = 300
    max_time_to_wait = 1800
    error_message_str = "Something went wrong"
    is_error_announced = False
    while True:
        try:
            question = generate_single_question()
            pop_question_window()
            is_error_announced = False
        except requests.exceptions.ConnectionError as e:
            if not is_error_announced:
                    pop_error_window()
                    is_error_announced = True
