from flask import Flask, jsonify, request
import psycopg2

try:
    connection = psycopg2.connect(database = "postgres",
                            user = "postgres",
                            password = "postgres",
                            host = "postgres",
                            port = "5432")
    print("Database connected successfully")
except:
    print("Database NOT connected successfully")

app = Flask(__name__)
db = connection.cursor()

@app.route('/', methods = ['GET'])
def get_counter():
    db.execute("SELECT * FROM counter")
    return 'Counter: {}'.format(db.fetchone()[0]) # Showing the counter

@app.route('/', methods = ['DELETE'])
def delete_counter():
    try:
        db.execute("DELETE FROM counter") # Deleting the actual counter
        db.execute("INSERT INTO counter VALUES (0)") # Inserting a new counter with 0 in its value
        return jsonify({'result': True})
    except:
        connection.rollback() # Setting the previous state
        return jsonify({'result': False})

@app.route('/<int:value>', methods = ['PUT'])
def update_counter(value):
    db.execute("UPDATE counter SET value = {}".format(value)) # Updating the counter value
    db.execute("SELECT * FROM contador")
    return jsonify({'contador': db.fetchone()[0]})

@app.route('/', methods = ['POST'])
def add_counter():
    counter_value = request.json['counter'] # Getting the new counter value from the json received
    db.execute("DELETE FROM counter") # Deleting the actual counter
    db.execute("INSERT INTO counter VALUES ({})".format(counter_value)) # Adding the new counter (a counter with the specified value)
    return jsonify({'counter': counter_value})
