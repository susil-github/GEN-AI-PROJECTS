'''
This file is responsible for invoking the openai api tpo get the llm response.
'''

from openai import OpenAI
import os
from dotenv import load_dotenv
from dbutil import execute_query, get_schema

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
schema = get_schema('emp')

while True:
    question = input('Ask any question !')
    if question == 'exit':
        break
    prompt = f'''
              You are SQL expert and you have access to the following database schema.:
              {schema}
              Do not provide any explanation or any other text. Only generate the sql
              that answers the question
              Question:{question}
    '''

response = client.responses.create(model='gpt-5', input=prompt)
result = response.output_text
print(f'Response is :{result}')
output = execute_query(result)
print(f'\n\n{output}')