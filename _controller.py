from flask import Flask, jsonify, request
from model.df_chat_model import get_answers
from model.ai_asistant_chat_model import get_ai_response
from model.osc_server_model import control_server
from tinydb import TinyDB, Query
from flask_cors import CORS

# init Flask app
app = Flask(__name__)
CORS(app)

# Route to get all items
@app.route('/get-muse-data', methods=['GET'])
def get_items():
    return jsonify({
        "result": "successful", 
        "message": "WSocket sercvice started"}), 200


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


# groq AI chat assistant
@app.route('/osc_stream', methods=['GET'])
def enable_osc_stream():
    # db = TinyDB('config.json')
    cmd = request.args.get('cmd')
    if cmd == "start":
        # db.truncate()
        # db.insert({ 'isOSCServiceStarted': True })

        control_server(cmd)
        
        # value = db.all()[0]['isOSCServiceStarted']
        return jsonify({
            "result": "successful", 
            "OSCServiceStarted": "value"}), 200

    if cmd == "stop":
        # db.truncate()
        # db.insert({ 'isOSCServiceStarted': False })

        control_server(cmd)

        # value = db.all()[0]['isOSCServiceStarted']
        return jsonify({
            "result": "successful", 
            "OSCServiceStarted": "value"}), 200

    


if __name__ == '__main__':
    app.run(debug=True)