from datetime import datetime

class FuzzyTime(object):
    _version = '0.01'

    def __init__(self, textual_release_date, start_release_date=None, end_release_date=None):
        filtered_release_date = textual_release_date
        filtered_start_release_date = start_release_date
        filtered_end_release_date = end_release_date

        self.textual_release_date = filtered_release_date
        self.certainty = 100
        self.start_release_date = start_release_date
        self.end_release_date = end_release_date

    def __str__(self):
        return self.textual_release_date