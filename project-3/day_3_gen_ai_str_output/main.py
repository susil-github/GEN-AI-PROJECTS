from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

client = OpenAI()

class SQLOutput(BaseModel):
    sql:str
    explanation: str=Field(description='This should have explanation of answer generated')
    operation_type:Literal['INSERT', 'DELETE','SELECT','UPDATE']
    tables_used:list[str]
    filters_used:list[str]
    clarity:int = Field('Rate the user questions on the clarity', ge=1, le=10)


histroy = []
histroy.append({'role':'system','content':'am a professional data engineer.'})
while True:
    input_msg = input('enter your question-:')
    histroy.append({'role':'user','content':input_msg})
    if input_msg == 'exit':
        break
    response = client.responses.parse(
        model ='gpt-5.6-sol',
        input=input_msg,
        text_format= SQLOutput
    )
    histroy.append({'role':'assistant','content':response.output_text})
    result = response.output_parsed
    print(result.sql,"\n")
    print(result.explanation,"\n")
    print(result.operation_type,"\n")
    print(result.tables_used,"\n")
    print(result.filters_used, "\n")
    print(result.clarity, "\n")