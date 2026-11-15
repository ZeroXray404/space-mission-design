"""
Classes and functions for keeping score
"""


class Score:
    def __init__(self):
        self.score = None

    def update_score(self, score_delta):
        self.score += score_delta # Addition or subtraction to current score

    def read_score(self):
        return self.score
