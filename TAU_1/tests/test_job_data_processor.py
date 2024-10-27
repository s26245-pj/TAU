import unittest
from unittest.mock import patch, MagicMock
from job_data_processor import JobDataProcessor
from job_data_reader import JobDataReader, Job

class TestJobDataProcessor(unittest.TestCase):

    def setUp(self):
        self.reader = JobDataReader()
        self.mock_jobs = [
            Job(2024, 'SE', 'FT', 'Data Engineer', 100000, 'USD', 100000, 'US', 100, 'US', 'L'),
            Job(2024, 'MI', 'PT', 'Data Scientist', 120000, 'USD', 120000, 'US', 0, 'US', 'M'),
            Job(2024, 'EN', 'FT', 'AI Engineer', 150000, 'USD', 150000, 'US', 50, 'US', 'S')
        ]
        self.reader._JobDataReader__jobs = self.mock_jobs

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=[
        Job(2024, 'SE', 'FT', 'Data Engineer', 100000, 'USD', 100000, 'US', 100, 'US', 'L'),
        Job(2024, 'MI', 'PT', 'Data Scientist', 120000, 'USD', 120000, 'US', 0, 'US', 'M'),
        Job(2024, 'EN', 'FT', 'AI Engineer', 150000, 'USD', 150000, 'US', 50, 'US', 'S')
    ])
    def test_filter_by_job_title(self, mock_get_jobs):
        jobs = JobDataProcessor.filter_by_job_title('Data Engineer')
        self.assertIsInstance(jobs, list)
        self.assertGreater(len(jobs), 0)
        for job in jobs:
            self.assertEqual(job.job_title.lower(), 'data engineer')

    @patch('job_data_reader.JobDataReader.get_jobs', return_value=[
        Job(2024, 'SE', 'FT', 'Data Engineer', 100000, 'USD', 100000, 'US', 100, 'US', 'L'),
        Job(2024, 'MI', 'PT', 'Data Scientist', 120000, 'USD', 120000, 'US', 0, 'US', 'M'),
        Job(2024, 'EN', 'FT', 'AI Engineer', 150000, 'USD', 150000, 'US', 50, 'US', 'S')
    ])
    def test_sort_by_salary(self, mock_get_jobs):
        jobs = JobDataProcessor.sort_by_salary('yes')
        self.assertIsInstance(jobs, list)
        self.assertGreater(len(jobs), 0)
        self.assertTrue(all(jobs[i].salary <= jobs[i + 1].salary for i in range(len(jobs) - 1)))

    def test_sort_invalid_ascending(self):
        with self.assertRaises(RuntimeError):
            JobDataProcessor.sort_by_salary('invalid')

if __name__ == '__main__':
    unittest.main()
