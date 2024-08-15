import subprocess
import os
from flask import Flask, jsonify, request
# from osc_config import enable_connectivity

# init Flask app
app = Flask(__name__)

# Example data
data = [
    {"id": 1, "name": "Item 1", "price": 100},
    {"id": 2, "name": "Item 2", "price": 150},
]

# Route to get all items
@app.route('/get-muse-data', methods=['GET'])
def get_items():
    err_message = {"result": "unsuccessful", "message": "Some error occurred"}
    valid_message = {"result": "successful", "message": "WSocket sercvice started"}
    return jsonify(valid_message), 200

if __name__ == '__main__':
    app.run(debug=True)