from db import MongoDriver
import json
from flask import Flask, Response, request, jsonify

app = Flask(__name__)
mongodb = MongoDriver()

@app.route('/obtener_datos', methods=['GET'])

def obtener_datos():
    datos = []
    for documento in mongodb.consult():
        datos.append({
            'Precio': documento['precio'],
            'Titulo': documento['titulo']
        })
    return jsonify({'datos': datos})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
