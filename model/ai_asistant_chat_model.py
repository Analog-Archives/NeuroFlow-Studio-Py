# Default
import os
from groq import Groq
from tinydb import TinyDB

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_ai_response(question):
    db = TinyDB('model/chat_db/ai_assistant_chat_history.json')

    if len(db.all()) == 0:
        db.insert({'role': "system", 'content': "you are a helpful assistant. Generate short and brief professional answers with less that 30 words."})
        
    db.insert({'role': "user", 'content': str(question)})

    chat_completion = client.chat.completions.create(
        messages = db.all(),
        model=os.environ.get("MODEL_NAME"),
    )

    # print(chat_completion.choices[0].message.content)
    db.insert({'role': "assistant", 'content': str(chat_completion.choices[0].message.content)})

    return (chat_completion.choices[0].message.content)

