from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv('gemini_api_key'))
question = 'tell me about genai in 10 words'
response = client.models.generate_content(model='gemini-3.5-flash', contents=question)
result = response.text
print(f'final result-:{result}')