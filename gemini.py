from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#testing testing testing

skills = "Python, Javascript, SQL"
exeprience = "built python weather app using API"
location = "Orlando, FLorida"
degree = "Undergrad"

prompt = f"A {degree} student is looking to build a new project to show off their knowledge. Please give 3 project ideas they can do to build their rersume. Skill: {skills} Experience: {exeprience}."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)