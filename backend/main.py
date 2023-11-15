from flask import Flask, request, jsonify
from flask_cors import CORS
from send_data import process_data
import json

app = Flask(__name__)
CORS(app, origins='http://localhost:4200')

@app.route('/users', methods=['POST'])
def handle_nodes():
    input_data = request.get_json()
    process_data(input_data)
    return jsonify({'message': 'Datos procesados con éxito'}), 200

@app.route('/users', methods=['GET'])
def get_nodes():
    with open('../data/response.json', 'r') as f:
        nodes_data = json.load(f)
    return jsonify(nodes_data), 200

if __name__ == '__main__':
    app.run(debug=True)