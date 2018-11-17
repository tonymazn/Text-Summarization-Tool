from summa.summarizer import summarize
from string import punctuation


def getsummary(text):
    text = sanitize(text)
    summary = summarize(text)
    return summary

def sanitize(text):
    removechartlist = {
        ord('\f') : ' ',
        ord('\t') : ' ',
        ord('\n') : ' ',
        ord('\r') : None
    }
    return text.translate(removechartlist)

