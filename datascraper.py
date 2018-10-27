from urllib import urlopen
from bs4 import BeautifulSoup
import re

def scrapeTable(url):

	html = urlopen(url)

	bsObj = BeautifulSoup(html, "lxml")

	data = bsObj.findAll("td")
	
	for line in data:
		stat = re.findall(r'"[a-z_]+"', str(line))
		value = line.get_text()

		column = stat[0][1:-1]

		print column, value

scrapeTable("https://www.pro-football-reference.com/years/2017/rushing.htm")
