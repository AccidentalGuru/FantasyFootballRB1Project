from bs4 import BeautifulSoup
from urllib import urlopen
import mysql.connector
import re

# Get URLs to scrape

def geturls():
	start_year = 2000
	end_year = 2018
	prefix = "https://www.pro-football-reference.com/years/"
	suffix = "/rushing.htm"

	urls = []

	for number in range(start_year, end_year):
		url = prefix + str(number) + suffix

		urls.append(url)

	return urls

# Iterate through URLs, scrape data, and save in list

def scrapeurls():

	urls = geturls()

	contents = []

	for url in urls:
		html = urlopen(url)

		bsObj = BeautifulSoup(html, "lxml")

		data = bsObj.findAll("td")

		year = int(''.join(re.findall(r"[\d]", url)))

		for line in data:
			stat = re.findall(r'"[a-z_]+"', str(line))
			value = line.get_text()
			column = stat[0][1:-1]

			data = re.sub(r'\*|\+|\%', "", value)

			if data == "":
				contents.append("0")

			elif column == "player":
				contents.append((data, year))

			else:
				contents.append(data)

	return contents

# Iterate through list of data and post to database

def postToDB():
	cnx = mysql.connector.connect(user ='xxxxx', password = 'xxxxx',
		host = 'xxxxx', database = 'xxxxx')

	cursor = cnx.cursor()

	contents = scrapeurls()

	index = 0

	for item in contents:

		try:

			year = contents[index+0][1]
			player = contents[index+0][0]
			team = contents[index+1]
			age = contents[index+2]
			pos = contents[index+3].capitalize()
			g = contents[index+4]
			gs = contents[index+5]
			rush_att = contents[index+6]
			rush_yds = contents[index+7]
			rush_td = contents[index+8]
			rush_long = contents[index+9]
			rush_yds_per_att = contents[index+10]
			rush_yds_per_g = contents[index+11]
			rush_att_per_g = contents[index+12]
			targets = contents[index+13]
			rec = contents[index+14]
			rec_yds = contents[index+15]
			rec_yds_per_rec = contents[index+16]
			rec_td = contents[index+17]
			rec_long = contents[index+18]
			rec_per_g = contents[index+19]
			rec_yds_per_g = contents[index+20]
			catch_pct = contents[index+21]
			touches = contents[index+22]
			yds_per_touch = contents[index+23]
			yds_from_scrimmage = contents[index+24]
			rush_receive_td = contents[index+25]
			fumbles = contents[index+26]

			index = index + 27

			# This needs PEP-8
			cursor.execute('INSERT INTO rushing_data (year, player, team, age, pos, g, gs, rush_att, rush_yds, rush_td, rush_long, rush_yds_per_att, rush_yds_per_g, rush_att_per_g, targets, rec, rec_yds, rec_yds_per_rec, rec_td, rec_long, rec_per_g, rec_yds_per_g, catch_pct, touches, yds_per_touch, yds_from_scrimmage, rush_receive_td, fumbles) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");' % (year, player, team, age, pos, g, gs, rush_att, rush_yds, rush_td, rush_long, rush_yds_per_att, rush_yds_per_g, rush_att_per_g, targets, rec, rec_yds, rec_yds_per_rec, rec_td, rec_long, rec_per_g, rec_yds_per_g, catch_pct, touches, yds_per_touch, yds_from_scrimmage, rush_receive_td, fumbles))
			cnx.commit()

			print "SUCCESS!", player, year

		# There's no utility for this error, so passing.
		except Exception as e:
			pass

postToDB()

