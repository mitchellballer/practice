from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

"""
#map incoming GET '/' request to hello function
@app.route("/")
def hello():
    #return simple json object
    return jsonify({'text':'Hello World!'})
"""

#Resource parameter contains incoming REST API call information
class Employees(Resource):

    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

#create REST API route mapping
#so navigating to server-url/employees will call get() function
api.add_resource(Employees, '/employees')
if __name__ == '__main__':
    app.run(port=5002)