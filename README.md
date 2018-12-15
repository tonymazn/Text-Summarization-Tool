CS410 Final Project - Text Summarization Tool
-
This tool is a Python base tool demonstrate EXTRACTIVE SUMMARIZATION by couple algorithms(such as LexRank, Luhn, LSA, TextRank). The input is plain text, and output is the summary text. Getting the tool to work is simple, download/clone the package, and go to the cs410-master folder and run the following command:
Step 1
python
>>>import nltk
>>>nltk.download()                              # install all the packages

Step 2
```
python setup.py install
```
System structure
-



    .
    ├─ cs410-master 
    │    └─── web
    │          ├── templates
    │          │     └── index.html
    │          ├── __init__.py
    │          └── webserver.py                  # Flask 1.0.2(1) entrance point
    ├── core
    │     ├── __init__.py
    │     ├── algorithms.py
    │     ├── preprocess.py
    │     ├── summarizer.py                      # Main function to generate summary result by using bs4(2) and SUMY(3)
    │     └── textsummarize.py                   # Pass summary result service for web 
    ├── tests 
    │     ├───── ROUGE_result                    # Create measure scores by pyrouge 0.1.3(4)
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

Usage Examples
-
```
Running local Flask web server:
    python -m web.webserver

Open web browser and type the following URL:
    http://localhost:5000

```
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
*  (1) Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks. https://pypi.org/project/Flask/
*  (2) Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work. https://www.crummy.com/software/BeautifulSoup/
*  (3) Simple library and command line utility for extracting summary from HTML pages or plain texts. The package also contains simple evaluation framework for text summaries. https://pypi.org/project/sumy/
*  (4) pyrouge is a Python wrapper for the ROUGE summarization evaluation package. Getting ROUGE to work can require quite a bit of time. pyrouge is designed to make getting ROUGE scores easier by automatically converting your summaries into a format ROUGE understands, and automatically generating the ROUGE configuration file. https://pypi.org/project/pyrouge/


