# -*- coding: utf-8 -*-

from .preprocess import get_parser
from .algorithms import algorithms
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer


def get_algorithm(algorithm_name):
    print('parameter:')
    print(algorithm_name)
    summarizer = None
    if algorithm_name == algorithms.LAS.value:
        summarizer = LsaSummarizer()
        print(algorithms.LAS.value)
    elif algorithm_name == algorithms.LexRank.value:
        summarizer = LexRankSummarizer()
        print(algorithms.LexRank.value)
    elif algorithm_name == algorithms.Luhn.value:
        summarizer = LuhnSummarizer()
        print(algorithms.Luhn.value)
    else:
        summarizer = TextRankSummarizer()
        print(algorithms.TextRank.value)
    return summarizer



def get_summary_result(text, count, algorithm_name):
    parser = get_parser(text)
    summarizer = get_algorithm(algorithm_name)
    return summarizer(parser.document, count)  

def convert_to_text(summarizer):
    result = ''
    for sentence in summarizer:
        result = result + str(sentence)
        print(sentence)
    return result

    