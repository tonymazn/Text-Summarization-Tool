CS410 Final Project - Text Summarization Tool
=============================================

This tool is a Python base tool demonstrate EXTRACTIVE SUMMARIZATION by couple algorithms.
Getting the tool to work is simple, download/clone the package, and go to the cs410-master
folder and run the following command:

python setup.py install


System structure
-----------------
cs410-master
    - web
	    - templates
		    index.html
		__init__.py
		webserver.py       #Flask entrance point
	- core
	    __init__.py
		algorithms.py
		preprocess.py
		summarizer.py   #main function to generate summary result by using SUMY(1)
		textsummarize.py  #The get summary result service for web
	- tests
	    - ROUGE_result    
		    LexRank.tet  #Lex Rank algorithm test log  
			LAS.txt      #LAS algorithm test log
			Luhn.txt     #Luhn algorithm test log
			TextRank.txt  #Text Rank algorithm test log
			ROUGE measure scores.pdf  #ROUGE measure scores report
		__init__.py
		evaluation.py
		runsystem.py   #execute the 
		settting.ini
		utils.py
README.md
requirements.txt
setup.cfg
setup.py


Usage Examples
--------------
python -m web.webserver




Reference
--------
(1) Simple library and command line utility for extracting summary from HTML pages or plain texts. The package also contains simple evaluation framework for text summaries, https://pypi.org/project/sumy/
