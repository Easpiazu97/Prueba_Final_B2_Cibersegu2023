"""
Se importa la clase MongoDriver desde el módulo db. Esto sugiere que hay un módulo db que contiene una 
implementación de una clase para interactuar con una base de datos MongoDB.
"""
from db import MongoDriver
import json
from flask import Flask, Response, request, jsonify


"""
Se crea una instancia de la aplicación Flask llamada app.
"""
app = Flask(__name__)
"""
También se crea una instancia de MongoDriver llamada mongodb. 
Esto asume que la clase MongoDriver proporciona métodos para consultar la base de datos MongoDB.
"""
mongodb = MongoDriver()

"""
Se define una función obtener_datos como una vista que se activa cuando se accede a la ruta
/obtener_datos mediante un método GET.
"""
@app.route('/obtener_datos', methods=['GET'])

""""
Dentro de esta función, se realiza una consulta a la base de datos MongoDB utilizando la instancia mongodb.
Se asume que mongodb.consult() devuelve una lista de documentos de la base de datos.
""""
def obtener_datos():
"""
Los datos de los documentos se extraen y se almacenan en una lista datos, 
donde cada elemento es un diccionario con las claves "Precio" y "Titulo".
"""
    datos = []
    for documento in mongodb.consult():
        datos.append({
            'Precio': documento['precio'],
            'Titulo': documento['titulo']
        })
    """
    Finalmente, los datos se devuelven como una respuesta JSON utilizando jsonify.
    """
    return jsonify({'datos': datos})

"""
Esta parte del código verifica si el script se está ejecutando directamente (no importado como un módulo). Si es así, inicia la aplicación Flask en el host '127.0.0.1' y 
el puerto 5000 con la opción de depuración activada (debug=True).
"""
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
