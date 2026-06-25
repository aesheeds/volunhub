from format import display_jobs
import io
import sys

def test_display_no_jobs():
    # Capture the output of the display_jobs function
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function with an empty list
    display_jobs([])

    # Restore stdout
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()

    assert "No jobs found." in output
    print("PASS: Empty job list test")


def test_display_one_job():
    job = [{
        "job_title": "Software Engineer Intern",
        "employer_name": "Google",
        "job_city": "Atlanta",
        "job_employment_type": "Internship",
        "job_salary_string": "$30/hr",
        "job_apply_link": "https://google.com"
    }]

    captured_output = io.StringIO()
    sys.stdout = captured_output

    display_jobs(job)

    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()

    assert "Software Engineer Intern" in output
    assert "Google" in output

    print("PASS: Single job test")

def test_missing_fields():
    job = [{
        "job_title": "Analyst"
    }]

    captured_output = io.StringIO()
    sys.stdout = captured_output

    display_jobs(job)
    
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()

    assert "Analyst" in output
    assert "Unknown" in output

    print("PASS: Missing fields test")

if __name__ == "__main__":
    test_display_no_jobs()
    test_display_one_job()
    test_missing_fields()