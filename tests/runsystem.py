# -*- coding: utf-8 -*-

import unittest
import os.path
from core.summarizer import *
from core.algorithms import algorithms
from .utils import *

class runsystem(unittest.TestCase):
    def test_generate_lexrank_summary(self):
        generate_summary(algorithms.LexRank, "system_lexrank")

    def test_generate_luhn_summary(self):
        generate_summary(algorithms.Luhn, "system_luhn")

    def test_generate_las_summary(self):
        generate_summary(algorithms.LAS, "system_las")

    def test_generate_textrank_summary(self):
        generate_summary(algorithms.TextRank, "system_textrank")



def generate_summary(algorithm, system_folder_name):
    test_data_path = "C:\\CS410\\Data\\duc2004_2\\testdata\\"
    cluster_folder = get_dir_list(test_data_path)
    for dir in cluster_folder:
        cluster_whole_path = os.path.join(os.path.dirname(test_data_path), dir)
        print(cluster_whole_path)
        dirs = get_file_list(cluster_whole_path)
        summary_result = ""
        for file in dirs:
            print("read file", end='')
            print(file)
            context = read_file(cluster_whole_path, file)
            summarizer = get_summary_result(context, 1, algorithm.value)
            summary_result +=convert_to_text(summarizer)
            summary_result +=get_newline()
            print(summary_result)
        create_file("C:\\CS410\\Data\\duc2004_2\\" + system_folder_name, dir.upper() + ".txt", summary_result)

if __name__ == '__main__':
    unittest.main()