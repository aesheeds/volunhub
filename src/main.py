# main.py
from database import save_user, get_user
from gemini import generate_search_query
from jsearch import send_query
from format import display_jobs
from parser import State

# Placeholders for future imports
# from parser import parse jsearch results

"""
Creates a new user profile by collecting all the required information
and storing it in Supabase. Returns the completed profile.
"""
def get_new_user():
    
    first_name = input("First name: ")
    last_name = input("Last name: ")
    degree = input("Degree: ")
    major = input("Major: ")
    skills = input("Skills: ")
    experience = input("Experience: ")
    location = input("Location: ")

    print("Job type:")
    print("1. Internship")
    print("2. Entry-level job")
    print("3. Either")

    job_type = input("Choose 1, 2, or 3: ")

    save_user(
        first_name,
        last_name,
        degree,
        major,
        skills,
        experience,
        location,
        job_type
    )

    return {
        "first_name": first_name,
        "last_name": last_name,
        "degree": degree,
        "major": major,
        "skills": skills,
        "experience": experience,
        "location": location,
        "job_type": job_type
    }

"""Determine whether a user already exists.
Retrieves an existing profile from Supabase or
creates a new profile if there is none found
"""
def get_profile():

    has_profile = input("Do you have an existing profile? (yes/no): ").lower()

    if has_profile == "yes":
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

        user = get_user(first_name, last_name)

        if user:
            print("Profile found.")
            return user
        
        print("Profile is not found. Creating a new profile")
    return get_new_user()

""" Controls the entire workflow of Jobhub.
The flow:
1. Retrieves/creates a user profile
2. Sends profile information to Gemini
3. Gemini generate a JSearch query 
4. JSearch return matching jobs
5. Parser cleans the response
6. Formatter displays the results"""
def main():
    # print("Welcome to Jobhub!")
    # profile = get_profile()

    S = State()
    S.display_state()   #welcome state
    S.display_state()   #credential state

    query = generate_search_query(
        S.data["first_name"],
        S.data["degree"],
        S.data["major"],
        S.data["skills"],
        S.data["experience"],
        S.data["location"],
        str(S.data["job_type"])
    )
    
    print("\nGenerated JSearch Query:")
    print(query)

    # need to add error checking here but I think it works for the most part
    raw_jobs = send_query(query)
    
    if not raw_jobs:
        print("Jsearch did not return return results.")
        return
    
    if "data" not in raw_jobs:
        print("Unexpected JSearch response:")
        print(raw_jobs)
        return

    jobs = raw_jobs["data"]["jobs"]

    display_jobs(jobs)
    
if __name__ == "__main__":
    main()