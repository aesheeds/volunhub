from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

# load supabase variables from .env file
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# funtion to add new user into database
def save_user(first_name, last_name, degree, major, skills, experience, location, job_type):
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "degree": degree,
        "major": major,
        "skills": skills,
        "experience": experience,
        "location": location,
        "job_type": job_type
    }
    response = supabase.table("users").insert(data).execute()
    return response

# function to get user information
def get_user(first_name, last_name):
    response = supabase.table("users").select("*").eq("first_name", first_name).eq("last_name", last_name).execute()
    if response.data:
        return response.data[0]
    return None

