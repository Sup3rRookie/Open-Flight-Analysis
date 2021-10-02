# Open-Flight-Analysis ✈️🌏
Maxis Case Study

## Tools used: 🛠️
- Python
- Pytest
- Sqlite3

## Thought process 🧠
- Considering the datasets haven't been update for quite a while
- The size of the data aren't too big
- Doesn't require to use a scheduler (Airflow / Luigi) to actively listen for a new incoming data.

Thus, it's easier to ingest the data in a local db and process it in csv format.

Otherwise, I might look into AWS RDS as it helps to:
- Handle large dataset efficiently
- Solve memory and performance issue
- Scalable and high availability

## Running the code 😉

Run the project with this command:
```bash
 cd to_my_project
 python main.py
```
To run the test file:
```bash
 python -m pytest --verbose
```
![App Screenshot](https://github.com/Sup3rRookie/Open-Flight-Analysis/blob/main/Unit_test_output.PNG?raw=true)

## Analysis 🔎
Find a column name for our csv data. It is available on their official website [here](https://openflights.org/data.html)

## Questions
### 1) Snapshot of the codes, and provide screenshot of SQL DDL
![App Screenshot](https://github.com/Sup3rRookie/Open-Flight-Analysis/blob/main/Creating%20table%20and%20insert%20values.PNG?raw=true)

### 2) How many airports there are in Malaysia.
Answer: 40

![App Screenshot](https://github.com/Sup3rRookie/Open-Flight-Analysis/blob/main/Question2%20-%20Output/TotalAirportsInMalaysia.PNG?raw=true)

### 3) Determine the distance in between the Malaysia airports
![App Screenshot](https://github.com/Sup3rRookie/Open-Flight-Analysis/blob/main/Question3%20-%20Output/DistanceBetweenAirportsInMalaysia.PNG?raw=true)

### 4) Determine how many flights are going to land in Malaysia’s airport in the next day during the point of query, and which airport is most congested based on the data.

Answer : 

166 flights going to land in Malaysia (KUL and PEN) on 2nd October 2021

Time of Query: 11.54pm on 1st of October 2021

Most congested airport: Kuala Lumpur International Airport.


#### Assumptions:
I only consider flights that are going to land at Malaysia's international airports which are (KLIA and PEN). Domestic airports are not included in the lists.