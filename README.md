CS410 Final Project - Text Summarization Tool
-
This project is a Python base tool to demonstrate TEXT SUMMARIZATION by couple algorithms(such as LexRank, Luhn, LSA, TextRank). The input is plain text, and output is the summary text. 

Installation
-
Getting the tool to work is simple, download/clone the package, and go to the cs410-master folder and then run the following command:


```
Step 1
python
>>>import nltk                                  # nltk(1) is Natural Language Toolkit
>>>nltk.download()                              # install all the packages

Step 2
python setup.py install
```

Start Instance
-
```
Running local Flask web server:
    python -m web.webserver

Open web browser and type the following URL:
    http://localhost:5000
```
	
System Structure
-



    .
    ├─ cs410-master 
    │    └─── web
    │          ├── templates
    │          │     └── index.html
    │          ├── __init__.py
    │          └── webserver.py                  # Flask 1.0.2(2) entrance point
    ├── core
    │     ├── __init__.py
    │     ├── algorithms.py
    │     ├── preprocess.py
    │     ├── summarizer.py                      # Main function to generate summary result by using bs4(3) and SUMY(4)
    │     └── textsummarize.py                   # Pass summary result service for web 
    ├── tests 
    │     ├───── ROUGE_result                    # Create measure scores by pyrouge 0.1.3(5)
    │     │         ├── LexRank.txt              # Lex Rank algorithm test log
    │     │         ├── LAS.txt                  # LAS algorithm test log 
    │     │         ├── Luhn.txt                 # Luhn algorithm test log 
    │     │         ├── TextRank.txt             # Text Rank algorithm test log 
    │     │         └── ROUGE measure scores.pdf # ROUGE measure scores report 
    │     ├── __init__.py
    │     ├── evaluation.py
    │     ├── runsystem.py                       # Generate summary system data
    │     ├── settting.ini 
    │     └── utils.py
    ├─ README.md
	├─ User Manual.pdf                           # User Manual
	├─ requirements.txt
    ├─ setup.cfg
    └─ setup.py


User Manual
-
https://github.com/tonymazn/cs410/blob/master/User%20Manual.pdf

Techniques Review
-
https://github.com/tonymazn/Text-Summarization-Techniques-Review/blob/master/Text%20Summarization%20Techniques%20Review.pdf

Version
-
0.0.1 

Team Member
-
Zhouning Ma

License
-
Apache License

Test Environment 1
-
http://mcsds.canadacentral.cloudapp.azure.com:5000


Test Environment 2
-
http://35.185.8.234:5000/

Reference
-
*  (1) NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum. https://www.nltk.org/
*  (2) Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks. https://pypi.org/project/Flask/
*  (3) Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work. https://www.crummy.com/software/BeautifulSoup/
*  (4) Simple library and command line utility for extracting summary from HTML pages or plain texts. The package also contains simple evaluation framework for text summaries. https://pypi.org/project/sumy/
*  (5) pyrouge is a Python wrapper for the ROUGE summarization evaluation package. Getting ROUGE to work can require quite a bit of time. pyrouge is designed to make getting ROUGE scores easier by automatically converting your summaries into a format ROUGE understands, and automatically generating the ROUGE configuration file. https://pypi.org/project/pyrouge/


