from job_data_reader import JobDataReader

class JobDataProcessor:

    @staticmethod
    def filter_by_job_title(job_title):
        try:
            jobs = JobDataReader().get_jobs()
            return [job for job in jobs if job.job_title.lower() == job_title.lower()]
        except Exception as e:
            raise RuntimeError(f"An error occurred during filtering by job title: {e}")

    @staticmethod
    def filter_by_experience_level(experience_level):
        try:
            jobs = JobDataReader().get_jobs()
            return [job for job in jobs if job.experience_level.lower() == experience_level.lower()]
        except Exception as e:
            raise RuntimeError(f"An error occurred during filtering by experience level: {e}")

    @staticmethod
    def filter_by_employment_type(employment_type):
        try:
            jobs = JobDataReader().get_jobs()
            return [job for job in jobs if job.employment_type.lower() == employment_type.lower()]
        except Exception as e:
            raise RuntimeError(f"An error occurred during filtering by employment type: {e}")

    @staticmethod
    def filter_by_work_year(work_year):
        try:
            jobs = JobDataReader().get_jobs()
            return [job for job in jobs if job.work_year == work_year]
        except Exception as e:
            raise RuntimeError(f"An error occurred during filtering by work year: {e}")

    @staticmethod
    def sort_by_salary(ascending):
        try:
            if ascending.lower() == "yes":
                ascending = True
            elif ascending.lower() == "no":
                ascending = False
            else:
                raise ValueError("Invalid value for ascending. Must be 'yes' or 'no'.")

            jobs = JobDataReader().get_jobs()
            return sorted(jobs, key=lambda job: job.salary, reverse=not ascending)
        except Exception as e:
            raise RuntimeError(f"An error occurred during sorting by salary: {e}")

    @staticmethod
    def sort_by_work_year(ascending):
        try:
            if ascending.lower() == "yes":
                ascending = True
            elif ascending.lower() == "no":
                ascending = False
            else:
                raise ValueError("Invalid value for ascending. Must be 'yes' or 'no'.")

            jobs = JobDataReader().get_jobs()
            return sorted(jobs, key=lambda job: job.work_year, reverse=not ascending)
        except Exception as e:
            raise RuntimeError(f"An error occurred during sorting by work year: {e}")

    @staticmethod
    def sort_by_job_title(ascending):
        try:
            if ascending.lower() == "yes":
                ascending = True
            elif ascending.lower() == "no":
                ascending = False
            else:
                raise ValueError("Invalid value for ascending. Must be 'yes' or 'no'.")

            jobs = JobDataReader().get_jobs()
            return sorted(jobs, key=lambda job: job.job_title, reverse=not ascending)
        except Exception as e:
            raise RuntimeError(f"An error occurred during sorting by job title: {e}")
