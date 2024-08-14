import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
from langchain_community.llms import Ollama 
import sqlite3
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
import os
from tinydb import TinyDB, Query

question = "Can you repeat the last question I asked ?"
guidelines = "just answer to the last question only while referring to the previous responses"
chat_history = [
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "How many 0 values in Delta_AF8 column",
        },
        {
            "role": "assistant",
            "content": "414",
        },
        {
            "role": "user",
            "content": "What's the name of the first column ?",
        },
        {
            "role": "assistant",
            "content": "The number of 0 values in Delta_AF8 column is 414.",
        },
        {
            "role": "user",
            "content": "The sum of the Delta_AF7 column ?" + guidelines,
        },
        {
            "role": "assistant",
            "content": "274.8186787477907",
        },
        {
            "role": "user",
            "content": "What's the first question I asked ?" + guidelines,
        },
        {
            "role": "assistant",
            "content": "The first question you asked was 'How many 0 values in Delta_AF8 column'",
        },
        {
            "role": "user",
            "content": "How many NaN values in the Battery column" + guidelines,
        },
        {
            "role": "assistant",
            "content": "62'",
        },
        {
            "role": "user",
            "content": "Is it ok if i delete these NaN values ?" + guidelines,
        }
]
llm = ChatGroq(
    model_name="llama-3.1-70b-versatile", api_key = os.getenv("GROQ_API_KEY"))

df = pd.read_csv('test/data.csv')
df = SmartDataframe(df, config={"llm": llm})

answer = df.chat(chat_history) 
print(" ")
print("--------------------------")
print(answer)