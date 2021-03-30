import random
encoding = 'utf-8'


class Question:
    shuffle_count = 10

    def __init__(self, question_str, category, answers):
        self._question_str = question_str
        self._category = category
        self._answers = answers
        self.shuffle_answers()

    def shuffle_answers(self):
        for i in range(self.shuffle_count):
            first = random.randint(0, len(self._answers) - 1)
            second = random.randint(0, len(self._answers) - 1)
            self.swap_answers(first, second)

    def swap_answers(self, first, second):
        temp = self._answers[first]
        self._answers[first] = self._answers[second]
        self._answers[second] = temp

    def is_correct_answer(self, index):
        return self._answers[index].get_is_correct()

    def __str__(self):
        return self._question_str

    def get_question_str(self):
        return self._question_str

    def get_correct_answer(self):
        for ans in self._answers:
            if ans.get_is_correct():
                return ans

    def get_correct_answer_str(self):
        for ans in self._answers:
            if ans.get_is_correct():
                return str(ans.get_answer_str(), encoding)

    def get_category(self):
        return self._category

    def get_answers_list(self):
        return self._answers

