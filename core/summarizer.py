# -*- coding: utf-8 -*-

from .preprocess import get_parser
from sumy.summarizers.lex_rank import LexRankSummarizer

def get_summary_result(text, count):
    parser = get_parser(text)
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, count)  
    result = ''
    for sentence in summary:
        result = result + str(sentence)
        print(sentence)
    return result
