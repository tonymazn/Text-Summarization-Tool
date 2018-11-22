# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'textsummarizetool',
    packages = find_packages(exclude=['unittest']),
    package_data = {
        'finalproject': ['README', 'LICENSE']
    },
    version = '0.0.1',
    description = 'A text summarization tool',
    long_description = open('README', encoding="utf-8").read(),
    author = 'Tony Ma',
    url = 'https://github.com/tonymazn/cs410',
    download_url = 'https://github.com/tonymazn/cs410/releases',
    keywords = ['text', 'nlp', 'summarization', "NLP","automatic summarization","keywords", "summary", "textrank", "pagerank","natural language processing",],
    install_requires = [
        'scipy >= 0.19',
        'flask>=1.0.2',
        'sumy>=0.7.0',
        'pyrouge>=0.1.3'
    ],
    python_requires = '>=3.4',
    test_suite = "unittest"
)
