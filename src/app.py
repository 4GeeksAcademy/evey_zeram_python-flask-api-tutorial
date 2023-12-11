from flask import Flask, jsonify, request
# defines flask y abajo 
# importas una variable de flask
app = Flask(__name__)

# @app.route('/myroute', methods=['GET'])
# def hello_world():
#     return 'Hello, World!'
# esta clase tiene un método y ruta [es lista]
@app.route('/todos', methods=['GET'])
def hello_world():
    my_json = jsonify(todos)
    return  my_json

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    response_body = jsonify(todos)
    return response_body, 200

#request es una librería y el data es el método
# a veces se le llama data = request.data

    # truco
    # @app.route('/todos', methods=['GET'])
    # def handle_todos():
    # response_body=todos
    # return response_body
    #data devuelve string, json diccionario
    # nosotros somos los que decimos qué enviar en el back
#cuidado con el DELETE el la app route. Position es una variable
# dentro de la función, mismo nombre
#int se pone porque defines el tipo

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    response_body = todos
    return response_body


some_data = {"name": "Bobby", "lastname": "Rixer"}
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
# si es un string devuelve HTML





# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

  # {diccionario} [lista]