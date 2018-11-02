import mysql.connector

cnx = mysql.connector.connect(user ='xxxxx', password = 'xxxxx',
host = 'xxxxx', database = 'xxxxx')
cursor = cnx.cursor()

# Function iterating through each player name, generating a
# unique list of the names, assigning an int value and then
# committing to the DB.

def generate_player_ids():
	league_type = "Standard"
	cursor.execute('select player from rushing_data')
	result = cursor.fetchall()

	name_holder = []

	for name in result:
		name_holder.append(name[0])
	
	for number, name in enumerate(set(name_holder), 1):
		cursor.execute('INSERT INTO player_ids (player_id, player) VALUES ("%s", "%s");' %
			(number, name))
		cnx.commit()
		print number, name, "ADDED SUCCESSFULLY"

generate_player_ids()
