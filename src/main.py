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
@staticmethod
def list_of_malaysia_airports() -> None:
	''' Display all airports in Malaysia.'''
	results = cursor.execute("SELECT * from OpenFlights WHERE Country = 'Malaysia' ORDER by 'City' LIMIT 120")
	return results.fetchall()

@staticmethod
def count_all_airports_in_malaysia() -> None:
	''' Total airports in Malaysia.'''
	results = cursor.execute("SELECT DISTINCT count(*) from OpenFlights WHERE Country = 'Malaysia' ORDER by 'City' LIMIT 120")
	return results.fetchall()

@lru_cache(maxsize=None)
def distance_between_each_airports() -> None:
	'''Determine the distance in between the Malaysia airports'''
	results = cursor.execute("SELECT Name,City,Latitude, Longitude from OpenFlights WHERE Country = 'Malaysia' order by 'City' LIMIT 120")
	airports = list(results)
	first_airport = (airports[0][-2], airports[0][-1])
	source = airports[0][0]

	for airport in airports:
		destination = airport[0]
		second_airport = (airport[-2], airport[-1])
		total_distance = f'{(geodesic(first_airport, second_airport).km):.2f}'
		result = print(f'From {source} to {destination}. The distance is {total_distance}km')
	return result

""" Function called"""
# list_of_malaysia_airports()
# count_all_airports_in_malaysia()
distance_between_each_airports()
conn.commit()
conn.close()