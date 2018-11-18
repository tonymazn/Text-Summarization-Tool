# -*- coding: utf-8 -*-

from pyrouge import Rouge155


def testresult():
    r = Rouge155()
    r.system_dir = 'C:/CS410/Data/duc2004_2/system'
    r.model_dir = 'C:/CS410/Data/duc2004_2/models'
    r.system_filename_pattern = 'D(\d+)T.TextRank.txt'
    r.model_filename_pattern = 'D#ID#.M.100.T.[A-D]'

    output = r.convert_and_evaluate()
    print(output)
    output_dict = r.output_to_dict(output)


if __name__ == '__main__':
    testresult()