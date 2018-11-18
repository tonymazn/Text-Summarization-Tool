# -*- coding: utf-8 -*-

from pyrouge import Rouge155


def lexrank_testresult():
    r = Rouge155()
    r.system_dir = 'C:/CS410/Data/duc2004_2/system_lexrank'
    r.model_dir = 'C:/CS410/Data/duc2004_2/models'
    r.system_filename_pattern = 'D(\d+)T.txt'
    r.model_filename_pattern = 'D#ID#.M.100.T.[A-Z]'

    output = r.convert_and_evaluate()
    print(output)
    output_dict = r.output_to_dict(output)

def luhn_testresult():
    r = Rouge155()
    r.system_dir = 'C:/CS410/Data/duc2004_2/system_luhn'
    r.model_dir = 'C:/CS410/Data/duc2004_2/models'
    r.system_filename_pattern = 'D(\d+)T.txt'
    r.model_filename_pattern = 'D#ID#.M.100.T.[A-Z]'

    output = r.convert_and_evaluate()
    print(output)
    output_dict = r.output_to_dict(output)

def las_testresult():
    r = Rouge155()
    r.system_dir = 'C:/CS410/Data/duc2004_2/system_las'
    r.model_dir = 'C:/CS410/Data/duc2004_2/models'
    r.system_filename_pattern = 'D(\d+)T.txt'
    r.model_filename_pattern = 'D#ID#.M.100.T.[A-Z]'

    output = r.convert_and_evaluate()
    print(output)
    output_dict = r.output_to_dict(output)

def textrank_testresult():
    r = Rouge155()
    r.system_dir = 'C:/CS410/Data/duc2004_2/system_textrank'
    r.model_dir = 'C:/CS410/Data/duc2004_2/models'
    r.system_filename_pattern = 'D(\d+)T.txt'
    r.model_filename_pattern = 'D#ID#.M.100.T.[A-Z]'

    output = r.convert_and_evaluate()
    print(output)
    output_dict = r.output_to_dict(output)


if __name__ == '__main__':
    lexrank_testresult()
    luhn_testresult()
    las_testresult()
    textrank_testresult()