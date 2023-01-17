import streamlit as st

st.title('ChatBot')

import openai
openai.api_key = "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"

prompt = (f"Write a story about an adventure")
text_input=st.text_input('Enter a prompt')

completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=text_input,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)


message = completions.choices[0].text
st.write(message)
