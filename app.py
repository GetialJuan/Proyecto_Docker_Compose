import time

from flask import Flask
import psycopg2

intento = True
while intento:
    try:
        conn = psycopg2.connect(database="postgres",
                                user="postgres",
                                password="postgres",
                                host="postgres",
                                port="5432")
        intento = False
        print("Database connected successfully")
    except:
        print("Database NOT connected successfully")
        intento = True

app = Flask(__name__)
db = conn.cursor()

@app.route('/')
def hello():
    db.execute("SELECT * FROM contador")
    return 'Contador: {}'.format(db.fetchone())
