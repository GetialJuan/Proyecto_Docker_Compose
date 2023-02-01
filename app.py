import time

from flask import Flask, jsonify, request
import psycopg2

try:
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="postgres",
                            host="postgres",
                            port="5432")
    print("Database connected successfully")
except:
    print("Database NOT connected successfully")

app = Flask(__name__)
db = conn.cursor()

@app.route('/', methods=['GET'])
def getContador():
    db.execute("UPDATE contador SET contador = (contador + 1)") # Aumenta el contador
    db.execute("SELECT * FROM contador") # Se obtiene el contador
    return 'Contador: {}'.format(db.fetchone()[0]) # Se muestra el contador

@app.route('/', methods=['DELETE'])
def deleteContador():
    db.execute("DELETE FROM contador") # Eliminamos el contador
    db.execute("INSERT INTO contador (contador) VALUES (0)") # Insertamos un nuevo contador en 0
    return jsonify({'result': True})

@app.route('/<int:valor>', methods=['PUT'])
def updateContador(valor):
    db.execute("UPDATE contador SET contador = {}".format(valor)) # Actualizamos el contador
    db.execute("SELECT * FROM contador") # Se obtiene el contador
    return jsonify({'contador': db.fetchone()[0]})

@app.route('/', methods=['POST'])
def addContador():
    newContador = request.json['contador'] # Se recibe el contador nuevo
    db.execute("DELETE FROM contador") # Se elimina el contador actual
    db.execute("INSERT INTO contador (contador) VALUES ({})".format(newContador)) # Se añade el nuevo contador
    return jsonify({'contador': newContador})
