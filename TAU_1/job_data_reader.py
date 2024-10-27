from typing import Any
import pandas as pd


class Job:
    def __init__(self, work_year, experience_level, employment_type, job_title, salary, salary_currency, salary_in_usd,
                 employee_residence, remote_ratio, company_location, company_size):
        self.work_year = work_year
        self.experience_level = experience_level
        self.employment_type = employment_type
        self.job_title = job_title
        self.salary = salary
        self.salary_currency = salary_currency
        self.salary_in_usd = salary_in_usd
        self.employee_residence = employee_residence
        self.remote_ratio = remote_ratio
        self.company_location = company_location
        self.company_size = company_size

    def __str__(self):
        return f"{self.work_year} | {self.experience_level} | {self.employment_type} | {self.job_title} | {self.salary} | {self.salary_currency} | {self.salary_in_usd} | {self.employee_residence} | {self.remote_ratio} | {self.company_location} | {self.company_size}"


class JobDataReaderMeta(type):
    _instances = {}

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in self._instances:
            instance = super().__call__(*args, **kwds)
            self._instances[self] = instance
        return self._instances[self]


class JobDataReader(metaclass=JobDataReaderMeta):
    def __init__(self) -> None:
        self.__jobs = []

    def read(self, path) -> None:
        try:
            print(f"Reading data from {path}")
            df = pd.read_csv(path, encoding='ISO-8859-1')

            for index, row in df.iterrows():
                self.__jobs.append(
                    Job(
                        work_year=row['work_year'],
                        experience_level=row['experience_level'],
                        employment_type=row['employment_type'],
                        job_title=row['job_title'],
                        salary=row['salary'],
                        salary_currency=row['salary_currency'],
                        salary_in_usd=row['salary_in_usd'],
                        employee_residence=row['employee_residence'],
                        remote_ratio=row['remote_ratio'],
                        company_location=row['company_location'],
                        company_size=row['company_size']
                    )
                )

            print(f"Read {len(self.__jobs)} jobs from {path}")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")
        except KeyError as e:
            raise KeyError(f"Missing expected column: {e}")

    def get_jobs(self) -> list[Job]:
        return self.__jobs