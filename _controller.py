from flask import Flask, jsonify, request
from model.df_chat_model import get_answers
from model.ai_asistant_chat_model import get_ai_response
from tinydb import TinyDB, Query
from flask_cors import CORS

# init Flask app
app = Flask(__name__)
CORS(app)

# Route to get all items
@app.route('/get-muse-data', methods=['GET'])
def get_items():
    return jsonify({"result": "successful", "message": "WSocket sercvice started"}), 200


# pandas AI chat
@app.route('/get-df-pandas-data', methods=['GET'])
def get_df_data():
    question = request.args.get('question')
    response = get_answers(question)
    if response:
        return jsonify({"result": "successful", "data": str(response)}), 200
    else:
        return jsonify({"result": "unsuccessful", "data": "no data found"}), 500


# groq AI chat assistant
@app.route('/get-ai-assistant', methods=['GET'])
def get_ai_assistant():
    question = request.args.get('question')
    response = get_ai_response(question)
    if response:
        return jsonify({"result": "successful", "data": str(response)}), 200
    else:
        return jsonify({"result": "unsuccessful", "data": "no data found"}), 500


if __name__ == '__main__':
    app.run(debug=True)