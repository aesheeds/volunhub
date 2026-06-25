from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# function to generate search query 
# no edge cases tests yet
def generate_search_query(first_name, degree, major, skills, experience, location, job_type):
    if job_type == "1":
        job_label = "internship"
    elif job_type == "2":
        job_label = "entry-level job"
    else:
        job_label = "internship or entry-level job"
    
    # prompt = f"""
    #         A {degree} student named {first_name} is looking for an {job_label}.
    #         Their info includes:
    #         Major: {major}
    #         Skills: {skills} 
    #         Experience: {experience}
    #         Location to Work: {location}. 
    #         Generate a short job search (10 words max) query for a job search API. Include what you think is most important and will
    #         generate the best job postings. Return only the query. No punctuation, No quotes. 
    #         """
    
    # gemini_models = ["gemini-2.5-flash", "gemini-3.5-flash"]

    # # try different models if one fails
    # for model in gemini_models:

    #     # try three times if gemini gives an error
    #     for attempt in range(3):
    #         try:
    #             response = client.models.generate_content(
    #                 model=model,
    #                 contents=prompt
    #             )
    #             return response.text.strip()

    #         except Exception as e:
    #             print(f"{model} attempt {attempt + 1} failed, Retrying . . .")
    #             time.sleep(20)

    print("Fall back response...")
    if skills:       
        skill_list = skills.split(",")[0].strip()
    else:
        skill_list = ''

    return f"{job_label} {major} {skill_list} {location}"
