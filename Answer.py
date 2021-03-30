class Answer:

    def __init__(self, answer_str, is_correct):
        self._answer_str = answer_str
        self._is_correct = is_correct

    def get_index(self):
        return self._index

    def get_is_correct(self):
        return self._is_correct

    def __str__(self):
        return self._answer_str

    def get_answer_str(self):
        return self._answer_str
