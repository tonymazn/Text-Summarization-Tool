# -*- coding: utf-8 -*-

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer



def get_parser(text):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    return parser
