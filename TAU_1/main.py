from job_data_reader import JobDataReader
from job_data_processor import JobDataProcessor
from job_data_visualizer import JobDataVisualizer
import messages

def print_jobs(jobs, batch_size=100):
    # Define column widths
    col_widths = {
        "work_year": 6,
        "experience_level": 16,
        "employment_type": 16,
        "job_title": 20,
        "salary": 10,
        "salary_currency": 8,
        "salary_in_usd": 14,
        "employee_residence": 16,
        "remote_ratio": 13,
        "company_location": 18,
        "company_size": 12
    }

    header = (
        "Year".ljust(col_widths["work_year"]) + " | " +
        "Experience Level".ljust(col_widths["experience_level"]) + " | " +
        "Employment Type".ljust(col_widths["employment_type"]) + " | " +
        "Job Title".ljust(col_widths["job_title"]) + " | " +
        "Salary".ljust(col_widths["salary"]) + " | " +
        "Currency".ljust(col_widths["salary_currency"]) + " | " +
        "Salary in USD".ljust(col_widths["salary_in_usd"]) + " | " +
        "Residence".ljust(col_widths["employee_residence"]) + " | " +
        "Remote Ratio".ljust(col_widths["remote_ratio"]) + " | " +
        "Company Location".ljust(col_widths["company_location"]) + " | " +
        "Company Size".ljust(col_widths["company_size"])
    )
    print(f"Number of jobs: {len(jobs)}")
    print(header)
    print("-" * len(header))

    for index, job in enumerate(jobs):
        print(
            str(job.work_year).ljust(col_widths["work_year"]) + " | " +
            job.experience_level.ljust(col_widths["experience_level"]) + " | " +
            job.employment_type.ljust(col_widths["employment_type"]) + " | " +
            job.job_title.ljust(col_widths["job_title"]) + " | " +
            str(job.salary).ljust(col_widths["salary"]) + " | " +
            job.salary_currency.ljust(col_widths["salary_currency"]) + " | " +
            str(job.salary_in_usd).ljust(col_widths["salary_in_usd"]) + " | " +
            job.employee_residence.ljust(col_widths["employee_residence"]) + " | " +
            str(job.remote_ratio).ljust(col_widths["remote_ratio"]) + " | " +
            job.company_location.ljust(col_widths["company_location"]) + " | " +
            job.company_size.ljust(col_widths["company_size"])
        )
        if (index + 1) % batch_size == 0:
            input("Press Enter to continue...")
    print("\n")

if __name__ == "__main__":
    dr = JobDataReader()
    dr.read(r'data.csv')

    print("Hello! Welcome to the job database. Type 'start'.")
    while True:
        prompt = input()
        if prompt == "start":
            break
        elif prompt == "exit":
            print("Thank you for using the job database. Goodbye!")
            exit()
        else:
            print("Invalid command. Please type 'start' to begin or 'exit' to quit.")

    running = True
    while running:
        try:
            print(messages.AVAILABLE_COMMANDS)
            prompt = input("What would you like to do?\n")

            if prompt == "filter":
                filter_type = input("What would you like to filter by? (Type the number)\n1. job_title\n2. experience_level\n3. employment_type\n4. work_year\n")
                if filter_type == "job_title" or filter_type == "1":
                    filter_value = input("What job title would you like to filter by? (e.g., Data Engineer, AI Engineer, Software Engineer)\n")
                    jobs = JobDataProcessor.filter_by_job_title(filter_value)
                elif filter_type == "experience_level" or filter_type == "2":
                    filter_value = input("What experience level would you like to filter by? (e.g., SE, MI, EN, EX)\n")
                    jobs = JobDataProcessor.filter_by_experience_level(filter_value)
                elif filter_type == "employment_type" or filter_type == "3":
                    filter_value = input("What employment type would you like to filter by? (e.g., FT, PT, CT, FL)\n")
                    jobs = JobDataProcessor.filter_by_employment_type(filter_value)
                elif filter_type == "work_year" or filter_type == "4":
                    filter_value = input("What work year would you like to filter by? (e.g., 2022, 2023, 2024)\n")
                    jobs = JobDataProcessor.filter_by_work_year(int(filter_value))
                else:
                    print("Invalid filter type. Please try again.")
                    continue

                print_jobs(jobs)

            elif prompt == "sort":
                sort_type = input("What would you like to sort by? (Type the number)\n1. salary\n2. work_year\n3. job_title\n")
                sort_asc = input("Would you like to sort in ascending order? (yes/no)\n")

                if sort_type == "salary" or sort_type == "1":
                    jobs = JobDataProcessor.sort_by_salary(sort_asc)
                elif sort_type == "work_year" or sort_type == "2":
                    jobs = JobDataProcessor.sort_by_work_year(sort_asc)
                elif sort_type == "job_title" or sort_type == "3":
                    jobs = JobDataProcessor.sort_by_job_title(sort_asc)
                else:
                    print("Invalid sort type. Please try again.")
                    continue

                print_jobs(jobs)

            elif prompt == "visualize":
                print("What would you like to visualize? Type the number of the option you'd like to choose.")
                print(messages.AVAILABLE_VISUALIZATIONS)

                visualization = input()

                if visualization == "1":
                    JobDataVisualizer.plot_jobs_per_year()
                elif visualization == "2":
                    JobDataVisualizer.plot_jobs_by_experience_level()
                elif visualization == "3":
                    job_title = input("Which job title would you like to visualize the average salary for?\n")
                    JobDataVisualizer.plot_average_salary_by_job_title(job_title)
                elif visualization == "4":
                    JobDataVisualizer.plot_average_salary_by_experience_level()
                elif visualization == "5":
                    JobDataVisualizer.plot_jobs_by_employment_type()
                elif visualization == "6":
                    JobDataVisualizer.plot_remote_jobs_ratio()
                else:
                    print("Invalid visualization. Please try again.")
            elif prompt == "exit":
                print("Thank you for using the job database. Goodbye!")
                running = False
            else:
                print("Invalid command. Please try again.")
        except Exception as e:
            print(e)
