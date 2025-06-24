import psycopg2
from psycopg2.extras import RealDictCursor
from configparser import ConfigParser
from functools import cache
import json


'''
Database.ini-file in use:
[postgresql]
host=localhost
database=assessment
port=5432
user=postgres
password=****
'''

# defines parser configuration
def config(filename='src/data/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db= {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


# store connection between calls
@cache
def get_conn():
  return psycopg2.connect(**config())


# add row to database
def db_add_row(fligh_number, departure_time, arrival_time, departure_airport, destination_airport):
    with get_conn() as conn:
        cursor = conn.cursor(cursor_factory = RealDictCursor)
        SQL = "INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport)" \
              "VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(SQL, (fligh_number, departure_time, arrival_time, departure_airport, destination_airport))
        conn.commit()
        result = {"success": "created flight number : %s " % fligh_number}
        cursor.close()
        return json.dumps(result)

def hello(name: str):
    return f'Hello {name}, this is a test :-)'

# order by departure time
def order_by_departure():
    with get_conn() as conn:
        cursor = conn.cursor(cursor_factory = RealDictCursor)
        SQL = "SELECT * FROM flights ORDER BY departure_time ASC"
        cursor.execute(SQL)
        data = cursor.fetchall()
        cursor.close()
        return json.dumps({'Ordered_flight_info': data}, default=str, indent=1)
 

# V  BONUS PYTHON TASK  V

# retrieves flight data ordered by airline (alphabetically)
def order_by_airline():
    with get_conn() as conn:
        cursor = conn.cursor(cursor_factory = RealDictCursor)
        SQL = "SELECT a.name AS airline_name, f.flight_number, f.departure_time, " \
              "f.departure_airport, f.arrival_time, f.destination_airport " \
              "FROM flights f RIGHT JOIN airlines a ON f.id = a.flights_id ORDER BY a.name ASC;"                
        cursor.execute(SQL)
        data = cursor.fetchall()
        cursor.close()
        return json.dumps({'Ordered_flight_info': data}, default=str, indent=1)

 

def db_delete_flight(id):
    con = psycopg2.connect(**config())
    cursor = con.cursor(cursor_factory=RealDictCursor)
    SQL = "DELETE FROM flights WHERE id = %s;"
    cursor.execute(SQL, (id,))
    con.commit()
    cursor.close()
    result = {"success": "deleted flight id: %s " % id}
    return json.dumps(result)

# This is for testing git commits :-)

if __name__ == '__main__':

    # used for testing, remove hashes to execute commands

    #db_add_row('AJ2475', '2025-08-10 12:00:00', '2025-08-10 13:00:00', 'Oslo Airport', 'Arlanda Airport')
    #db_add_row('VD0847', '2025-04-28 09:15:00', '2025-04-29 11:45:00', 'Heathrow Airport', 'Auckland Airport')
    #db_add_row('YT7842', '2025-11-14 11:30:00', '2025-11-14 13:00:00', 'Roma Airport', 'Wien Airport')
    #db_delete_flight(8)
    
    hello('Filip')
