# -*- coding: utf-8 -*-


from string import punctuation
from .summarizer import get_summary_result

def replace(text):
    text = text.replace("\r","")
    text = text.replace("\n","")
    return text

def sanitize(text):
    removechartlist = {
        ord('\f') : ' ',
        ord('\t') : ' ',
        ord('\n') : ' ',
        ord('\r') : None
    }
    return text.translate(removechartlist)

def get_summary(text):
    return get_summary_result(text)



