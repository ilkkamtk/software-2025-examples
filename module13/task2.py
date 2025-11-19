from flask import Flask, request
from flask_cors import CORS
import mysql.connector

connection = mysql.connector.connect(
    host='mysql.metropolia.fi',
    port=3306,
    database='ilkkamtk',
    user='ilkkamtk',
    password='q1w2e3r4',
    autocommit=True
)

def get_airport_by_icao_code(icao_code):
    sql = f"SELECT * FROM airport WHERE ident='{icao_code}'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/airport/<icao>')
def get_airport(icao):
    airport = get_airport_by_icao_code(icao)
    if airport is None:
        return {'message': 'Airport not found'}, 404
    return airport

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)