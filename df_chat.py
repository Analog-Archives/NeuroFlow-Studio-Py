# 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

import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
from langchain_community.llms import Ollama 
import sqlite3
import os

llm = ChatGroq(model_name="llama-3.1-70b-versatile", api_key = "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")

df = pd.read_csv('data.csv')
df = SmartDataframe(df, config={"llm": llm})

question = "How many 0 values in Delta_AF8 column"
answer = df.chat(question) 
print(answer)