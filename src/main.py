# main.py
from database import save_user, get_user
from gemini import generate_search_query
from jsearch import send_query

# Placeholders for future imports
# from parser import parse jsearch results
# from format import display jobs

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
    print("Welcome to Jobhub!")
    
    profile = get_profile()

    query = generate_search_query(
        profile["first_name"],
        profile["degree"],
        profile["major"],
        profile["skills"],
        profile["experience"],
        profile["location"],
        profile["job_type"]
    )
    
    print("\nGenerated JSearch Query:")
    print(query)

    raw_jobs = send_query(query)
    print(raw_jobs)

    # Future integration:
    #parser
    #formatter

if __name__ == "__main__":
    main()