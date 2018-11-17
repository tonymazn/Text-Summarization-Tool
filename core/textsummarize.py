# -*- coding: utf-8 -*-

from summa.summarizer import summarize
from string import punctuation

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
    text = sanitize(text)
    text = replace(text)
    summary = summarize(text)
    summary = sanitize(summary)
    summary = replace(summary)
    return summary



