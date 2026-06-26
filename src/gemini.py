from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# function to generate search query
# no edge cases tests yet


def generate_search_query(first_name, degree,
                          major, skills, experience,
                          location, job_type):

    if job_type == "1":
        job_label = "internship"
    elif job_type == "2":
        job_label = "entry-level job"
    else:
        job_label = "internship or entry-level job"

    prompt = f"""
            You are a job search expert helping a student find jobs.
            
            Student Profile:
            - Name: {first_name}
            - Degree: {degree}
            - Major: {major}
            - Skills: {skills}
            - Experience: {experience}
            - Location: {location}
            - Job Type: {job_label}
            
            Your Tasks:
            - Based on a student's profile determine the 
              BEST job title that matches their background
            - Build a short search query (5-8 word) using that job title

            Rules:
            - Think about job titles that employers actually post for someone
              with these skills
            - Include location if specified (ex. not "Anywhere" or "Remote")
            - Return only the query. No punctuation, No quotes.
            - For internship, include "internship" in the query
            - Don't include job type in the query if it's "internship or entry-level job"

            Examples of good thinking:
            - Skills: C, Python, embedded systems -> 
              Job title: Embedded Software Engineer ->
              Query: Embedded Software Engineer Internship

            - Skills: React, JavaScript, CSS ->
              Job title: Frontend Developer ->
              Query: Frontend Developer Internship

            - Skills: SQL, Excel, Python ->
              Job title: Data Analyst ->
              Query: Data Analyst Internship Chicago

            Now generate the query
            """

    gemini_models = ["gemini-2.5-flash", "gemini-3.5-flash"]

    # try different models if one fails
    for model in gemini_models:

        # try three times if gemini gives an error
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                #print out query for debugging
                #print(response.text.strip())
                return response.text.strip()

            except Exception as e:
                print(f"{model} attempt {attempt + 1} failed, Retrying . . .")
                time.sleep(20)

    print("Fall back response...")
    if skills:
        skill_list = skills.split(",")[0].strip()
    else:
        skill_list = ''

    return f"{job_label} {major} {skill_list} {location}"
