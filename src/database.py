from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

# load supabase variables from .env file
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# funtion to add new user into database
def save_user(first_name, last_name, degree, major, skills, experience, location):
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "degree": degree,
        "major": major,
        "skills": skills,
        "experience": experience,
        "location": location
    }
    response = supabase.table("users").insert(data).execute()
    return response

# function to get user information
def get_user(first_name, last_name):
    response = supabase.table("users").select("*").eq("first_name", first_name).eq("last_name", last_name).execute()
    if response.data:
        return response.data[0]
    return None

# test test test
save_user("Shellsea", 
        "Nunez-Aviles", 
        "Undergraduate", 
        "Information Technology and Web Design", 
        "Python, React, JavaScript, SQL, HTML, CSS", 
        "UI/UX Case Study, Portoflio Website Using React, Voluntering Event Signup App usng React", 
        "Anywhere")

print(get_user("Shellsea", "Nunez-Aviles"))