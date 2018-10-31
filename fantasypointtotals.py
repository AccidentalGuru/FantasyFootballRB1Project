import mysql.connector

cnx = mysql.connector.connect(user ='xxxxx', password = 'xxxxx',
host = 'xxxxx', database = 'xxxxx')
cursor = cnx.cursor()

# Function for calculating total year's point, standard scoring

def standard_league():
	league_type = "Standard"
	cursor.execute('select * from rushing_data')
	result = cursor.fetchall()

	pts_rush_yard = 0.1
	pts_rush_td = 6
	pts_rec_yards = 0.1
	pts_rec_td = 6
	pts_fumble = -2

	for row in result:
		year = row[0]
		player = row[1]
		team = row[2]
		age = row[3]
		g = row[5]
		gs = row[6]
		rush_yds = row[8]
		rush_tds = row[9]
		rush_yds_per_g = row[12]
		rush_att_per_g = row[13]
		targets = row[14]
		rec = row[15]
		rec_yds = row[16]
		rec_tds = row[18]
		touches = row[23]
		rush_receive_td = row[25]
		fumbles = row[27]

		total_fantasy_score = ((rush_yds * pts_rush_yard) + (rush_tds * pts_rush_td) +
		(rec_yds * pts_rec_yards) + (rec_tds * pts_rec_td)) - (fumbles * pts_fumble)

		cursor.execute("""INSERT INTO annual_fantasy_totals (league_type, year, player, team, age,
			g, gs, rush_yds, rush_tds, rush_yds_per_g, rush_att_per_g, targets,
			rec, rec_yds, rec_tds, touches, fumbles, rush_receive_td, total_fantasy_score) VALUES ("%s",
			"%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",
			"%s","%s", "%s", "%s", "%s", "%s");""" % (league_type, year, player, team, age, g, gs, rush_yds,
				rush_tds, rush_yds_per_g, rush_att_per_g, targets, rec, rec_yds,
				rec_tds, touches, fumbles, rush_receive_td, total_fantasy_score))

		cnx.commit()

		print "Successfully added to database: ", player, year

# Function for calculating total year's point, half point PPR

def half_point_ppr():
	league_type = "Half Point PPR"
	cursor.execute('select * from rushing_data')
	result = cursor.fetchall()

	pts_rush_yard = 0.1
	pts_rush_td = 6
	pts_rec = 0.5
	pts_rec_yards = 0.1
	pts_rec_td = 6
	pts_fumble = -2

	for row in result:
		year = row[0]
		player = row[1]
		team = row[2]
		age = row[3]
		g = row[5]
		gs = row[6]
		rush_yds = row[8]
		rush_tds = row[9]
		rush_yds_per_g = row[12]
		rush_att_per_g = row[13]
		targets = row[14]
		rec = row[15]
		rec_yds = row[16]
		rec_tds = row[18]
		touches = row[23]
		rush_receive_td = row[25]
		fumbles = row[27]

		total_fantasy_score = ((rush_yds * pts_rush_yard) + (rush_tds * pts_rush_td) +
		(rec_yds * pts_rec_yards) + (rec_tds * pts_rec_td) + (rec * pts_rec)) - (fumbles * pts_fumble)

		cursor.execute("""INSERT INTO annual_fantasy_totals (league_type, year, player, team, age,
			g, gs, rush_yds, rush_tds, rush_yds_per_g, rush_att_per_g, targets,
			rec, rec_yds, rec_tds, touches, fumbles, rush_receive_td, total_fantasy_score) VALUES ("%s",
			"%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",
			"%s","%s", "%s", "%s", "%s", "%s");""" % (league_type, year, player, team, age, g, gs, rush_yds,
				rush_tds, rush_yds_per_g, rush_att_per_g, targets, rec, rec_yds,
				rec_tds, touches, fumbles, rush_receive_td, total_fantasy_score))

		cnx.commit()

		print "Successfully added to database: ", player, year
    
# Function for calculating total year's point, full point PPR

def full_point_ppr():
	league_type = "Full Point PPR"
	cursor.execute('select * from rushing_data')
	result = cursor.fetchall()

	pts_rush_yard = 0.1
	pts_rush_td = 6
	pts_rec = 1.0
	pts_rec_yards = 0.1
	pts_rec_td = 6
	pts_fumble = -2

	for row in result:
		year = row[0]
		player = row[1]
		team = row[2]
		age = row[3]
		g = row[5]
		gs = row[6]
		rush_yds = row[8]
		rush_tds = row[9]
		rush_yds_per_g = row[12]
		rush_att_per_g = row[13]
		targets = row[14]
		rec = row[15]
		rec_yds = row[16]
		rec_tds = row[18]
		touches = row[23]
		rush_receive_td = row[25]
		fumbles = row[27]

		total_fantasy_score = ((rush_yds * pts_rush_yard) + (rush_tds * pts_rush_td) +
		(rec_yds * pts_rec_yards) + (rec_tds * pts_rec_td) + (rec * pts_rec)) - (fumbles * pts_fumble)

		cursor.execute("""INSERT INTO annual_fantasy_totals (league_type, year, player, team, age,
			g, gs, rush_yds, rush_tds, rush_yds_per_g, rush_att_per_g, targets,
			rec, rec_yds, rec_tds, touches, fumbles, rush_receive_td, total_fantasy_score) VALUES ("%s",
			"%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",
			"%s","%s", "%s", "%s", "%s", "%s");""" % (league_type, year, player, team, age, g, gs, rush_yds,
				rush_tds, rush_yds_per_g, rush_att_per_g, targets, rec, rec_yds,
				rec_tds, touches, fumbles, rush_receive_td, total_fantasy_score))

		cnx.commit()

		print "Successfully added to database: ", player, year

# Single function posting all scoring totals back to the database

def generate_and_commit():
	print "Standard League Scoring: Querying stats, calculating scores, and writing to database..."
	standard_league()

	print "Half-Point PPR League Scoring: Querying stats, calculating scores, and writing to database..."
	half_point_ppr()

	print "Full-Point PPR League Scoring: Querying stats, calculating scores, and writing to database..."
	full_point_ppr()

generate_and_commit()
