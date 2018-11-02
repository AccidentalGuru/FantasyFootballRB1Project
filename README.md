# Fantasy Football RB1 Project

This is a complete, out-of-the-box webscraper and local database builder written in Python 2.7 (I know...I'll be updating my old-school self soon). Focusing exclusively on Fantasy Football runningback data, this script scrapes NFL rushing data from 2000 - 2017, extracts and cleans it, and then posts it back to a database.

## MacOS Instructions - Installing the necessary libraries:

**NOTE**: To install 'pip': https://pip.pypa.io/en/stable/installing/
**NOTE**: To install MySQL: https://dev.mysql.com/downloads/mysql/

1) Open Terminal
2) Copy and paste "make install"; hit enter/return

## MacOS Instructions - Creating the database and database table:

1) Open Terminal
2) Copy and paste "make initdb"; hit enter/return
3) Enter your password

## MacOS Instructions - Populating the database #1 (scraping year-end rushing stats via datascraper.py):

**NOTE**: The "start_year" and "end_year" variables are currently hard-coded to 2000 - 2017. You can change this to a year as far back as 1932. Simply update the int values for the noted variables on lines 11 & 12.

First, open this code in your code editor of choice. Be sure to update the values on lines 61 & 62 to ensure that you have the proper database credentials entered. Then, you can simply build your code from your editor or, you can save this file to your machine, open the Terminal and copy and paste "make collect_stats".

That should execute the code, which takes about 1-2 minutes to run to completion. There are prompts in the code to illustrate what's happening at each step.

## MacOS Instructions - Populating the database #2 (querying database and calculating totals via fantasypointtotals.py):

That should execute the code, which takes ~15 seconds to run to completion. There are prompts in the code to illustrate what's happening at each step.
