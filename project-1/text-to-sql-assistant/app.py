import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from dbutil import execute_query, get_schema

load_dotenv()
client = OpenAI()
st.title("text to sql assistant")
st.write("Welcome to my application")
question = st.text_input("enter your question")
schema = get_schema('emp')
prompt = f'''
              You are SQL expert and you have access to the following database schema.:
              {schema}
              Do not provide any explanation or any other text. Only generate the sql
              that answers the question
              Question:{question}
    '''
if st.button("submit"):
 response = client.responses.create(
 model='gpt-5',
 input= prompt
 )
 result = response.output_text
 st.write(result)
 output = execute_query(result)
 st.write(output)


