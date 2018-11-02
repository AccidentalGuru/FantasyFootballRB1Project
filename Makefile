START_YEAR=2000
END_YEAR=2017
collect_stats:
	python datascraper.py --startYear=${START_YEAR} --endYear=${END_YEAR}

collect_fantasy:
	python fantasypointtotals.py

install:
	pip install -Ur requirements.txt

initdb:
	mysql --user=root --password -s < create_database.sql
