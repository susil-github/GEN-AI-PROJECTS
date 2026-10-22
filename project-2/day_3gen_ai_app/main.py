from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
response_id = None
while True:
    input_msg = input("Enter the question here:->")
    if input_msg == 'exit':
        break
    response = client.responses.create(
        model='gpt-5',
        input=input_msg,
        previous_response_id=response_id
    )
    response_id = response.id
    print(response.output_text)


