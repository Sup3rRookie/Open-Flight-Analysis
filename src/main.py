import sqlite3, csv, pandas as pd

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

""" Alternative way to ingest csv data to db"""
# df = pd.read_csv('airports.csv')
# df.to_sql('Open Flights', conn, if_exists='append', index=False)

conn.commit()
conn.close()