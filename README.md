# Fantasy Football RB1 Project

This is a complete, out-of-the-box webscraper and local database builder written in Python 2.7 (I know...I'll be updating my old-school self soon). Focusing exclusively on Fantasy Football runningback data, this script scrapes NFL rushing data from 2000 - 2017, extracts and cleans it, and then posts it back to a database.

## MacOS Instructions - Installing the necessary libraries:

**NOTE**: To install 'pip': https://pip.pypa.io/en/stable/installing/
**NOTE**: To install MySQL: https://dev.mysql.com/downloads/mysql/

1) Open Terminal
2) Copy and paste "pip install urllib"; hit enter/return
3) Copy and paste "pip install beautifulsoup4"; hit enter/return
4) Copy and paste "pip install mysql-connector==2.1.4"; hit enter/return

## MacOS Instructions - Creating the database and database table:

1) Open Terminal
2) Copy and paste "/usr/local/mysql/bin/mysql -u root -p"
3) Enter your password
4) Copy and paste "CREATE DATABASE **enter desired database name**;" and hit enter/return
5) Copy and paste "USE **enter database name**;" and hit enter/return
6) Copy and paste "CREATE TABLE **enter desired table name** (year int, player varchar(255), team varchar(255), age int, pos varchar(255), g int, gs int, rush_att int, rush_yds int, rush_td int, rush_long int, rush_yds_per_att float(4,2), rush_yds_per_g float(4,2), rush_att_per_g float(4,2), targets int, rec int, rec_yds int, rec_yds_per_rec float(4,2), rec_td int, rec_long int, rec_per_g float(4,2), rec_yds_per_g float(4,2), catch_pct float(4,2), touches int, yds_per_touch float(4,2), yds_from_scrimmage int, rush_receive_td int, fumbles int);" and hit enter/return
  
## MacOS Instructions - Populating the database #1 (scraping year-end rushing stats via datascraper.py):

**NOTE**: The "start_year" and "end_year" variables are currently hard-coded to 2000 - 2017. You can change this to a year as far back as 1932. Simply update the int values for the noted variables on lines 11 & 12.

First, open this code in your code editor of choice. Be sure to update the values on lines 61 & 62 to ensure that you have the proper database credentials entered. Then, you can simply build your code from your editor or, you can save this file to your machine, open the Terminal and copy and paste "python <file path for datascraper.py>".
  
That should execute the code, which takes <60 seconds to run to completion. There are prompts in the code to illustrate what's happening at each step.

## MacOS Instructions - Populating the database #2 (querying database and calculating totals via fantasypointtotals.py):

1) Open Terminal
2) Copy and paste "/usr/local/mysql/bin/mysql -u root -p"
3) Enter your password
4) Copy and paste "USE **enter database name**;" and hit enter/return
5) Copy and paste "CREATE TABLE **enter desired table name** (league_type varchar(255), year int, player varchar(255), team varchar(255), age int, g int, gs int, rush_yds int, rush_tds int, rush_yds_per_g float(5,2), rush_att_per_g float(5,2), targets int, rec int, rec_yds int, rec_tds int, rush_receive_td int, touches int, fumbles int, total_fantasy_score int);" and hit enter/return

Open this code in your code editor of choice. Be sure to update the values on lines 61 & 62 to ensure that you have the proper database credentials entered. Then, you can simply build your code from your editor or, you can save this file to your machine, open the Terminal and copy and paste "python <file path for datascraper.py>".
  
That should execute the code, which takes ~15 seconds to run to completion. There are prompts in the code to illustrate what's happening at each step.
