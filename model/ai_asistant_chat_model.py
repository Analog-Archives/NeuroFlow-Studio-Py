# Default
import os
from groq import Groq
from tinydb import TinyDB

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_ai_response(question):
    db = TinyDB('model/chat_db/ai_assistant_chat_history.json')
    db.insert({'role': "system", 'content': "you are a helpful assistant. Generate short and brief professional answers with less that 30 words."})
    db.insert({'role': "user", 'content': str(question)})

    chat_completion = client.chat.completions.create(
        # messages=[
        #     {
        #         "role": "system",
        #         "content": "you are a helpful assistant. Generate short and brief professional answers with less that 30 words."
        #     },
        #     {
        #         "role": "user",
        #         "content": "Explain the importance of fast language models",
        #     }
        # ],
        messages = db.all(),
        model="mixtral-8x7b-32768",
    )

    # print(chat_completion.choices[0].message.content)
    db.insert({'role': "assistant", 'content': str(chat_completion.choices[0].message.content)})

    return (chat_completion.choices[0].message.content)

