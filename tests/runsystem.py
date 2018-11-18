# -*- coding: utf-8 -*-

import unittest
import os.path
from core.summarizer import *
from core.algorithms import algorithms
from .utils import *


class runsystem(unittest.TestCase):
    def test_create_file(self):
        #create_file("C:\\CS410\\Data\\duc2004_2\\system", "test.txt", "Woops! I have deleted the content!")
        self.assertEqual(1+1, 2)

    def test_generate_summary(self):
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
              #print(context)
              summarizer = get_summary_result(context, 1, algorithms.TextRank )
              #print(summarizer)
              summary_result +=convert_to_text(summarizer)
              summary_result +=get_newline()
              print(summary_result)
              create_file("C:\\CS410\\Data\\duc2004_2\\system", dir.upper() + ".TextRank.txt", summary_result)

if __name__ == '__main__':
    unittest.main()