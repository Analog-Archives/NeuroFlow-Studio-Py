import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
from langchain_community.llms import Ollama 
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
import os
from tinydb import TinyDB

# db = TinyDB('model/chat_db/df_chat_history.json')  

def get_answers(question): 
    # global db 
    # db.insert = ({
    #     'role': 'user',
    #     'content': str(question)
    # })

    llm = ChatGroq(
        model_name="llama-3.1-70b-versatile", api_key = os.getenv("GROQ_API_KEY"))

    df = pd.read_csv('test/data.csv')
    df = SmartDataframe(df, config={"llm": llm})
    answer = df.chat(question) 
    
    # db.insert = ({
    #     'role': 'assistant',
    #     'content': str(answer)
    # })

    return str(answer)

# get_answers()