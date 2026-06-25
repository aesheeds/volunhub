# format.py

def display_jobs(jobs):
    """Displays job search results returned from
    JSearch in a clean command-line format.
    """
    if not jobs:
        print("No jobs found.")
        return
    print("\n===== Job Search Results =====\n")

    for index, job in enumerate(jobs, start=1):

        print(f"{index}. {job.get('job_title', 'No Title')}")

        print(
            f"  Company: "
            f"{job.get('employer_name', 'Unknown')}"
        )

        print(
            f"  Location: "
            f"{job.get('job_city', 'Unknown')}, "
        )

        if job.get("job_employment_type"):
            print(
                f"  Type: "
                f"{job.get('job_employment_type')}"
            )
        if job.get("job_salary_string"):
            print(
                f"  Salary: "
                f"{job.get('job_salary_string')}"
            )

        if job.get("job_apply_link"):
            print(
                f"  Apply: "
                f"{job.get('job_apply_link')}"
            )

        print()
