import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv() # Loads the .env file

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Hello, world!")
print(response.text)