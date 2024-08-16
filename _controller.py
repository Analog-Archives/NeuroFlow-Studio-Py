import subprocess
import os
from flask import Flask, jsonify, request
from model.df_chat_model import get_answers
from tinydb import TinyDB, Query

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

# pandas AI chat
@app.route('/get-df-data', methods=['GET'])
def get_df_data():
    question = request.args.get('question')
    
    db = TinyDB('model/chat_db/df_chat_history.json')
    db.insert({'role': 'user', 'content': str(question)})
    
    response = get_answers(question)
    if response:
        db.insert({'role': 'assistant', 'content': str(response)})
            
        return jsonify({"result": "successful", "data": str(response)}), 200
    else:
        return jsonify({"result": "unsuccessful", "data": "no data found"}), 500
if __name__ == '__main__':
    app.run(debug=True)