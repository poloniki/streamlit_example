import requests
import streamlit as st
url = "https://openai80.p.rapidapi.com/chat/completions"


def get_chat(text):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": f'''Give me how positive is this statement
                {text} on scale from 1 to 10. Only respond with a number!! Please."'''
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": st.secrets['key'],
        "X-RapidAPI-Host": st.secrets['host']
    }

    response = requests.post(url, json=payload, headers=headers)


    return response.json()['choices'][0]['message']['content']
