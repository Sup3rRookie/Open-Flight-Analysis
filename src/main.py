import sqlite3, csv, pandas as pd
from geopy.distance import geodesic
from functools import lru_cache

conn= sqlite3.connect('airport.db',  timeout=10)
cursor = conn.cursor()

""" Create table """
cursor.execute("""CREATE TABLE IF NOT EXISTS "Open Flights" (
	"AirportID"	TEXT,
	"Name"	TEXT,
	"City"	TEXT,
	"Country"	TEXT,
	"IATA"	TEXT,
	"ICAO"	REAL,
	"Latitude"	REAL,
	"Longitude"	INTEGER,
	"Altitude"	INTEGER,
	"Timezone"	TEXT,
	"DST"	TEXT,
	"Tzdatabasetimezone"	TEXT,
	"Type"	TEXT,
	"Source"	TEXT
)""")

""" Ingest csv data to db """
with open('airports.csv','r', encoding='utf-8') as f:
    dr = csv.DictReader(f) # comma is default delimiter
    to_db = [(i['AirportID'],i['Name'], i['City'],i['Country'], i['IATA'],i['ICAO'], i['Latitude'],i['Longitude'], i['Altitude'], i['Timezone'],i['DST'], i['Tzdatabasetimezone'], i['Type'], i['Source']) for i in dr]
cursor.executemany("INSERT INTO 'Open Flights' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", to_db)

""" Other ways to ingest csv data to db"""
# df = pd.read_csv('airports.csv')
# df.to_sql('Open Flights', conn, if_exists='append', index=False)

""" Analysis """
def list_of_malaysia_airports() -> list:
	""" Display all airports in Malaysia."""
	results = cursor.execute("SELECT * from OpenFlights WHERE Country = 'Malaysia' ORDER by 'City' LIMIT 120")
	return results.fetchall()

def count_all_airports_in_malaysia() -> int:
	""" Total airports in Malaysia."""
	results = cursor.execute("SELECT DISTINCT count(*) from OpenFlights WHERE Country = 'Malaysia' ORDER by 'City' LIMIT 120")
	return results.fetchall()[0][0]

@lru_cache(maxsize=None)
def distance_between_each_airports(departure_airport) -> dict:
	""" Determine the distance in between the Malaysia airports """
	results = cursor.execute("SELECT Name,City,Latitude, Longitude from OpenFlights WHERE Country = 'Malaysia' order by 'City' LIMIT 120")
	airports = list(results)
	try:
		klia = [i for i in airports if i[0] == departure_airport][0]
	except Exception as e:
		raise ValueError(f"Airport Not Found: {departure_airport}")
	klia_airport = (klia[-2],klia[-1])
	airport_distance = {}

	for airport in airports:
		destination = airport[0]
		second_airport = (airport[-2], airport[-1])
		total_distance = geodesic(klia_airport, second_airport).km
		airport_distance[destination] = total_distance
	return airport_distance

def print_distance_between_each_airports(departure_airport,airport_distance_dict):
	""" Print distance between airports """
	for arrival_airport, distance in airport_distance_dict.items():
		print(f'From {departure_airport} to {arrival_airport}. The distance is {distance:.2f}km')


# print(count_all_airports_in_malaysia())
print(list_of_malaysia_airports())
if __name__ == '__main__':
	""" Function called """
	# list_of_malaysia_airports()
	# count_all_airports_in_malaysia()
	# departure_airports = "Kuala Lumpur International Airportsss"
	# result = distance_between_each_airports(departure_airports)
	# print_distance_between_each_airports(departure_airports,result)
	conn.commit()
	conn.close()