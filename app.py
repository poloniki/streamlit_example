import streamlit as st
from apipred import get_chat

st.title('Chat GPT apps')



with st.form('form'):
    chat_input = st.text_input('Chat input')

    form_button = st.form_submit_button('Predict')


if form_button:
    text = get_chat(chat_input)
    st.metric(label="Positivity", value=text)
    st.warning('Please be aware - this can be wrong', icon="⚠️")
    st.balloons()



if 'number' not in st.session_state:
    st.session_state['number'] = 1

exmaple_button = st.button('Increment')

if exmaple_button:
    st.write(st.session_state['number'])
    st.session_state['number'] +=1
