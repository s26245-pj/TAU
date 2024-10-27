
import unittest
from unittest.mock import patch
from ..job_data_processor import JobDataProcessor
from ..job_data_visualizer import JobDataVisualizer
from ..job_data_reader import Job


sample_jobs = [
    Job(2023, "EN", "FT", "Data Engineer", 120000, "USD", 120000, "USA", 100, "USA", "L"),
    Job(2022, "MI", "PT", "AI Engineer", 90000, "USD", 90000, "CAN", 50, "CAN", "M"),
    Job(2021, "EX", "CT", "Software Engineer", 150000, "USD", 150000, "USA", 0, "USA", "S"),
    Job(2023, "SE", "FT", "Data Scientist", 115000, "USD", 115000, "USA", 100, "USA", "L"),
    Job(2023, "EN", "FL", "Web Developer", 60000, "USD", 60000, "MEX", 50, "MEX", "S"),
]


class JobDataProcessorTests(unittest.TestCase):

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=sample_jobs)
    def test_filter_by_job_title(self, mock_get_jobs):
        result = JobDataProcessor.filter_by_job_title("Data Engineer")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].job_title, "Data Engineer")
        self.assertEqual(result[0].experience_level, "EN")

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=sample_jobs)
    def test_filter_by_experience_level(self, mock_get_jobs):
        result = JobDataProcessor.filter_by_experience_level("EN")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].experience_level, "EN")
        self.assertEqual(result[1].experience_level, "EN")

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=sample_jobs)
    def test_filter_by_employment_type(self, mock_get_jobs):
        result = JobDataProcessor.filter_by_employment_type("FT")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].employment_type, "FT")
        self.assertEqual(result[1].employment_type, "FT")

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=sample_jobs)
    def test_filter_by_work_year(self, mock_get_jobs):
        result = JobDataProcessor.filter_by_work_year(2023)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].work_year, 2023)
        self.assertEqual(result[2].work_year, 2023)

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=sample_jobs)
    def test_sort_by_salary_ascending(self, mock_get_jobs):
        result = JobDataProcessor.sort_by_salary("yes")
        self.assertEqual(result[0].salary, 60000)
        self.assertEqual(result[-1].salary, 150000)
        self.assertTrue(result[0].salary < result[1].salary)

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=sample_jobs)
    def test_sort_by_salary_descending(self, mock_get_jobs):
        result = JobDataProcessor.sort_by_salary("no")
        self.assertEqual(result[0].salary, 150000)
        self.assertEqual(result[-1].salary, 60000)
        self.assertTrue(result[0].salary > result[1].salary)

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=sample_jobs)
    def test_sort_by_work_year_ascending(self, mock_get_jobs):
        result = JobDataProcessor.sort_by_work_year("yes")
        self.assertEqual(result[0].work_year, 2021)
        self.assertEqual(result[-1].work_year, 2023)
        self.assertTrue(result[0].work_year < result[1].work_year)

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=sample_jobs)
    def test_sort_by_job_title_ascending(self, mock_get_jobs):
        result = JobDataProcessor.sort_by_job_title("yes")
        self.assertEqual(result[0].job_title, "AI Engineer")
        self.assertEqual(result[-1].job_title, "Web Developer")
        self.assertTrue(result[0].job_title < result[1].job_title)

# Klasa testowa dla JobDataVisualizer
class JobDataVisualizerTests(unittest.TestCase):

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=sample_jobs)
    def test_plot_jobs_per_year(self, mock_get_jobs):
        try:
            JobDataVisualizer.plot_jobs_per_year()
            self.assertTrue(True)  # Metoda wykonała się bez błędów
        except Exception as e:
            self.fail(f"plot_jobs_per_year zgłosiło wyjątek: {e}")

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=sample_jobs)
    def test_plot_jobs_by_experience_level(self, mock_get_jobs):
        try:
            JobDataVisualizer.plot_jobs_by_experience_level()
            self.assertTrue(True)  # Metoda wykonała się bez błędów
        except Exception as e:
            self.fail(f"plot_jobs_by_experience_level zgłosiło wyjątek: {e}")

if __name__ == '__main__':
    unittest.main()
