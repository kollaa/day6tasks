from flask import Flask,jsonify,request
from flask_restful import Resource,Api 

app = Flask(__name__)
api = Api(app)

items =[]

class Student(Resource):
    def get(self,name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None }, 404 

    def post(self,name):
        data = request.get_json() 
        item = {'name': name ,'price': 12.00 }
        items.append(item)
        return item ,201

    

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Student, '/Student/<string:name>')
api.add_resource(ItemList, '/Student')

app.run(port = 5000 , debug = True )