from bs4 import BeautifulSoup
import urllib
import re

def generate_data(url):

	player_data_list = []

	open_stats_url = urllib.urlopen(url)
	player_data = BeautifulSoup(open_stats_url, 'html.parser')
	nr = re.compile(r'<.*?>')

	for value in player_data.find_all('td'):
		player_data_list.append(nr.sub('', str(value)))

	index = 0

	while index < 27:

		for number in range(index, len(player_data_list) + 1, 27):
			if number < (25 * 27):
				try:
					value = player_data_list[number]

					if index == 0: # Player Name
						print re.sub('[^a-zA-Z0-9]+', ' ', value)

					elif index ==1: # Player Team
						print value

					elif index == 2: # Player Age
						print value

					elif index == 4: # Number of Games Played
						print value

					elif index == 5: # Number of Games Started
						print value

					elif index == 6: # Total Rushing Attempts
						print value

					elif index == 7: # Total Rushing Yards
						print value

					elif index == 8: # Total Rushing Touchdowns
						print value

					elif index == 9: # Longest Rush Attempt
						print value

					elif index == 10: # Rush Yards per Attempt
						print value

					elif index == 11: # Rush Yard per Game
						print value

					elif index == 12: # Rush Attempts per Game
						print value

					elif index == 13: # Passing Targets
						print value

					elif index == 14: # Receptions
						print value

					elif index == 15: # Receiving Yards
						print value

					elif index == 16: # Yards per Reception
						print value

					elif index == 17: # Receiving Touchdowns
						print value

					elif index == 18: # Longest Pass Reception
						print value

					elif index == 19: # Receptions per Game
						print value

					elif index == 20: # Receiving Yards per Game
						print value

					elif index == 21: # Catch Percentage
						print value[0:4]

					elif index == 22: # Total Touches
						print value	

					elif index == 23: # Yards per Touch
						print value

					elif index == 24: # Total Scrimmage Yards
						print value

					elif index == 25: # Total Touchdowns
						print value

					elif index == 26: # Fumbles
						print value

					else:
						pass

				except:
					pass
			else:
				pass

		index += 1

def database_builder():
	stats_url_front = "https://www.pro-football-reference.com/years/"
	stats_url_back = "/rushing.htm"
	urls = []

	for number in range(2013, 2018):
		urls.append(stats_url_front + str(number) + stats_url_back)

	for url in urls:
		generate_data(url)


database_builder()

