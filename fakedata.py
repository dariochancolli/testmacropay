#Realizado por Dario Chan Colli

from http.client import responses
from multiprocessing import resource_tracker
from flask import Flask, request, render_template, render_template_string, jsonify, make_response
from flask_restful import Resource, Api
import json

with open('fakedatabase.js') as file: #La ruta depende de donde tengas almacenada la base de datos
    fakedata = json.load(file) 
req= sorted(fakedata, key=lambda x: x["name"])


app = Flask(__name__)
api = Api(app)


class contacts(Resource):
    def get(self):
        res= make_response(jsonify(req), 200)
        return res


class ContactData(Resource):
    def get(self, contact_id):
        ids=[]

        for i in range(len(req)):
            ids.append(fakedata[i].get('id'))
        for j in range(len(ids)):
            if contact_id==ids[j]:
                data=req[j]
                res= make_response(jsonify(data), 200)
                return res

        if contact_id is not ids:
            res= make_response(jsonify({'message': "Not found"}), 404)
            return res

class DeleteData(Resource):

    def get(self, contact_id):

        ids=[]
        
        for i in range(len(req)):
            ids.append(fakedata[i].get('id'))
        for j in range(len(ids)):
            if contact_id == ids[j]:
                req.pop(j)
                res= make_response(jsonify({'message': "NO CONTENT"}), 204)
                return res

            

        if contact_id is not ids:
            res= make_response(jsonify({'message': "NOT FOUND"}), 404)
            return res


api.add_resource(contacts, '/application/json')  # Route_1
api.add_resource(ContactData, '/application/json/contacts<contact_id>')  # Route_2
api.add_resource(DeleteData, '/application/json/contacteeeeee2s/<contact_id>')  # Route_3

if __name__ == '__main__':
    app.run(port='5000')

