# -*- coding: utf-8 -*-


from string import punctuation
from .summarizer import *


def get_summary(text, count, algorithm_name):
    return convert_to_text(get_summary_result(text, count, algorithm_name))

