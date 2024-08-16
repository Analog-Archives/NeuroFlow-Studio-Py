import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
from langchain_community.llms import Ollama 
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
import os
from tinydb import TinyDB

def get_answers(question):
    # chat history update
    db = TinyDB('model/chat_db/df_chat_history.json')
    db.insert({'role': 'user', 'content': str(question)})

    llm = ChatGroq(
        model_name = 
            os.environ.get("MODEL_NAME"), 
            api_key = os.getenv("GROQ_API_KEY"))

    df = pd.read_csv('test/data.csv')
    df = SmartDataframe(df, config={"llm": llm})

    instructions = "Don't generate any charts, just give the answer in a string format"

    answer = df.chat(question + instructions)
    
    # chat history update 
    db.insert({'role': 'assistant', 'content': str(answer)})

    return str(answer)