import streamlit as st

st.title('ChatBot')

import openai
openai.api_key = "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"

prompt = (f"Write a story about an adventure")
text_input=st.text_input('Enter a prompt')
t=st.slider('slide to set temperature value', min_value=0.1, max_value=1.0)
completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=text_input,
    max_tokens=inf,
    n=1,
    stop=None,
    temperature=0.5,
)


message = completions.choices[0].text
st.write(message)
