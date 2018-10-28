from urllib import urlopen
from bs4 import BeautifulSoup
import re

start_year = 2013
end_year = 2017

def scrapeTable(url):

	html = urlopen(url)

	bsObj = BeautifulSoup(html, "lxml")

	data = bsObj.findAll("td")
	
	for line in data:
		stat = re.findall(r'"[a-z_]+"', str(line))
		value = line.get_text()
		column = stat[0][1:-1]

		print column, re.sub(r'\*|\+', "", value)

def yearIterator():
	for number in range(start_year, end_year + 1):
		url = "https://www.pro-football-reference.com/years/" + str(number) + "/rushing.htm"

		scrapeTable(url)

