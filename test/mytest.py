import unittest

from summa.summarizer import summarize
from utils import get_text_from_test_data


class mytest(unittest.TestCase):
    def test_summary(self):
    # Test Summary result
        text = get_text_from_test_data("example.txt")
        print("*******************************************************************************")
        print(text)
        # Makes a summary of the text.
        generated_summary = summarize(text)
        print("*******************************************************************************")
        print(generated_summary)
        print("*******************************************************************************")
        self.assertNotEqual(generated_summary, "")

    def test_summary_ratio(self):
    # Test Summary result
        text = get_text_from_test_data("example.txt")
        print("*******************************************************************************")
        print(text)
        # Makes a summary of the text.
        generated_summary = summarize(text, ratio=0.1)
        print("*******************************************************************************")
        print(generated_summary)
        print("*******************************************************************************")
        self.assertNotEqual(generated_summary, "")

    def test_summary_words(self):
    # Test Summary result
        text = get_text_from_test_data("example.txt")
        print("*******************************************************************************")
        print(text)
        # Makes a summary of the text.
        generated_summary = summarize(text, words=25)
        print("*******************************************************************************")
        print(generated_summary)
        print("*******************************************************************************")
        self.assertNotEqual(generated_summary, "")

    def test_short_sentence(self):
        text = "A strong winter storm moving over the eastern half of the country has claimed at least eight lives and knocked out power for tens of thousands of people."
        generated_summary = summarize(text, n=4)
        print("*******************************************************************************")
        print(generated_summary)
        print("*******************************************************************************")
        self.assertNotEqual(generated_summary, "")


if __name__ == '__main__':
    unittest.main()