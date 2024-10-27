import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from job_data_reader import JobDataReader

class JobDataVisualizer:

    @staticmethod
    def plot_jobs_per_year():
        try:
            jobs = JobDataReader().get_jobs()
            work_years = [job.work_year for job in jobs]
            year_counts = Counter(work_years)

            years = sorted(year_counts.keys())
            counts = [year_counts[year] for year in years]

            plt.figure(figsize=(12, 6))
            plt.bar(years, counts, color='dodgerblue')
            plt.xlabel('Year')
            plt.ylabel('Number of Jobs')
            plt.title('Number of Jobs Per Year')
            plt.show()
        except Exception as e:
             raise RuntimeError(f"An error occurred during visualization of jobs per year: {e}")

    @staticmethod
    def plot_jobs_by_experience_level():
        try:
            jobs = JobDataReader().get_jobs()
            experience_levels = [job.experience_level for job in jobs]
            level_counts = Counter(experience_levels)

            levels = sorted(level_counts.keys())
            counts = [level_counts[level] for level in levels]

            plt.figure(figsize=(12, 6))
            plt.bar(levels, counts, color='mediumseagreen')
            plt.xlabel('Experience Level')
            plt.ylabel('Number of Jobs')
            plt.title('Number of Jobs by Experience Level')
            plt.show()
        except Exception as e:
            raise RuntimeError(f"An error occurred during visualization of jobs by experience level: {e}")

    @staticmethod
    def plot_average_salary_by_job_title(job_title):
        try:
            jobs = JobDataReader().get_jobs()
            title_jobs = [job for job in jobs if job.job_title.lower() == job_title.lower()]

            if not title_jobs:
                raise ValueError(f"No jobs found for title: {job_title}")

            salaries = [job.salary for job in title_jobs if job.salary != "Unknown"]
            avg_salary = np.mean(salaries)

            plt.figure(figsize=(12, 6))
            plt.barh([job_title], [avg_salary], color='lightcoral')
            plt.xlabel('Average Salary')
            plt.ylabel('Job Title')
            plt.title(f'Average Salary for {job_title}')
            plt.show()
        except Exception as e:
            raise RuntimeError(f"An error occurred during visualization of average salary for {job_title}: {e}")

    @staticmethod
    def plot_average_salary_by_experience_level():
        try:
            jobs = JobDataReader().get_jobs()
            levels = list(set([job.experience_level for job in jobs]))
            avg_salaries = []

            for level in levels:
                level_jobs = [job for job in jobs if job.experience_level == level]
                salaries = [job.salary for job in level_jobs if job.salary != "Unknown"]
                avg_salaries.append(np.mean(salaries))

            plt.figure(figsize=(12, 6))
            plt.bar(levels, avg_salaries, color='mediumpurple')
            plt.xlabel('Experience Level')
            plt.ylabel('Average Salary')
            plt.title('Average Salary by Experience Level')
            plt.show()
        except Exception as e:
            raise RuntimeError(f"An error occurred during visualization of average salary by experience level: {e}")

    @staticmethod
    def plot_jobs_by_employment_type():
        try:
            jobs = JobDataReader().get_jobs()
            employment_types = [job.employment_type for job in jobs]
            type_counts = Counter(employment_types)

            types = sorted(type_counts.keys())
            counts = [type_counts[etype] for etype in types]

            plt.figure(figsize=(12, 6))
            plt.bar(types, counts, color='skyblue')
            plt.xlabel('Employment Type')
            plt.ylabel('Number of Jobs')
            plt.title('Number of Jobs by Employment Type')
            plt.show()
        except Exception as e:
            raise RuntimeError(f"An error occurred during visualization of jobs by employment type: {e}")

    @staticmethod
    def plot_remote_jobs_ratio():
        try:
            jobs = JobDataReader().get_jobs()
            remote_ratios = [job.remote_ratio for job in jobs]
            remote_counts = Counter(remote_ratios)

            labels = ['On-site', 'Hybrid', 'Remote']
            sizes = [remote_counts.get(0, 0), remote_counts.get(50, 0), remote_counts.get(100, 0)]
            colors = ['lightcoral', 'gold', 'lightskyblue']
            explode = (0, 0.1, 0.1)

            plt.figure(figsize=(8, 8))
            plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
            plt.title('Remote Jobs Ratio')
            plt.show()
        except Exception as e:
            raise RuntimeError(f"An error occurred during visualization of remote jobs ratio: {e}")
