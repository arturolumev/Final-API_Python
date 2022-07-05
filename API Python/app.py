# from calendar import weekheader
# from dbm import dumb
# from http.client import ImproperConnectionState
# from json import dumps
# from urllib import response
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from colas import *

app = Flask(__name__)
# app.config['MONGO_URI']='mongodb://localhost/pymongodb'   mongodb://localhost:27017
app.config['MONGO_URI'] = 'mongodb://localhost/dbgrupal'

mongo = PyMongo(app)

cola = QueueLinkedListsCircular()

@app.route('/proyecto', methods=['POST'])
def create_proyect():
    titulo_pry = request.json['titulo_pry']
    descripcion_pry = request.json['descripcion_pry']
    requisitos_pry = request.json['requisitos_pry']
    pago_pry = request.json['pago_pry']
    vacantes_pry = request.json['vacantes_pry']

    if titulo_pry and descripcion_pry and requisitos_pry and pago_pry and vacantes_pry:
        id = mongo.db.proyecto.insert_one(
            {'titulo_pry': titulo_pry, 'descripcion_pry': descripcion_pry, 'requisitos_pry': requisitos_pry,
             'pago_pry': pago_pry, 'vacantes_pry': vacantes_pry}
        )
        response = {
            'id': str(id.inserted_id),
            'titulo_pry': titulo_pry,
            'descripcion_pry': descripcion_pry,
            'requisitos_pry': requisitos_pry,
            'pago_pry': pago_pry,
            'vacantes_pry': vacantes_pry
        }
        #print(response)
        #print(type(response))
        #cola.enQueue(response)

        return response
    else:
        {'mensaje': 'error'}

    return {'mensaje': 'recibido'}

@app.route('/proyectos', methods=['GET'])
def get_proyects():
    proyectos = mongo.db.proyecto.find()
    response = json_util.dumps(proyectos)

    res = json.loads(response)
    cola = QueueLinkedListsCircular()

    for i in range(0, len(res)):
        cola.enQueue(res[i])

    lista = []

    while cola.front is not None:
        lista.append(cola.front.data)
        cola.front = cola.front.next

    jsonString = json.dumps(lista)

    return Response(jsonString, mimetype='application/json')

@app.route('/proyecto/<id>', methods=['GET'])
def get_proyecto(id):
    proyecto = mongo.db.proyecto.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(proyecto)

    return Response(response, mimetype='application/json')


@app.route('/proyecto/<id>', methods=['DELETE'])
def delete_proyect(id):
    mongo.db.users.delete_one({'id': ObjectId(id)})
    response = jsonify({'message': 'Proyecto ' + id + ' elimiando'})
    return response


if __name__ == "__main__":
    app.run(debug=True)
