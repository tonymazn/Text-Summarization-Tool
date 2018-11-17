# -*- coding: utf-8 -*-


from string import punctuation
from .summarizer import get_summary_result

def get_summary(text, count, algorithm_name):
    return get_summary_result(text, count, algorithm_name)



