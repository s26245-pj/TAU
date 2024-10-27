import unittest
from unittest.mock import patch
from job_data_visualizer import JobDataVisualizer
from job_data_reader import Job

class TestJobDataVisualizer(unittest.TestCase):

    def setUp(self):
        self.mock_jobs = [
            Job(2024, 'SE', 'FT', 'Data Engineer', 100000, 'USD', 100000, 'US', 100, 'US', 'L'),
            Job(2024, 'MI', 'PT', 'Data Scientist', 120000, 'USD', 120000, 'US', 0, 'US', 'M'),
            Job(2024, 'EN', 'FT', 'AI Engineer', 150000, 'USD', 150000, 'US', 50, 'US', 'S')
        ]

    @patch('job_data_visualizer.plt.show')
    @patch('job_data_reader.JobDataReader.get_jobs', return_value=[
        Job(2024, 'SE', 'FT', 'Data Engineer', 100000, 'USD', 100000, 'US', 100, 'US', 'L'),
        Job(2024, 'MI', 'PT', 'Data Scientist', 120000, 'USD', 120000, 'US', 0, 'US', 'M'),
        Job(2024, 'EN', 'FT', 'AI Engineer', 150000, 'USD', 150000, 'US', 50, 'US', 'S')
    ])
    def test_plot_jobs_per_year(self, mock_get_jobs, mock_show):
        try:
            JobDataVisualizer.plot_jobs_per_year()
        except Exception:
            self.fail("plot_jobs_per_year() raised Exception unexpectedly!")

    @patch('job_data_visualizer.plt.show')
    @patch('job_data_reader.JobDataReader.get_jobs', return_value=[
        Job(2024, 'SE', 'FT', 'Data Engineer', 100000, 'USD', 100000, 'US', 100, 'US', 'L'),
        Job(2024, 'MI', 'PT', 'Data Scientist', 120000, 'USD', 120000, 'US', 0, 'US', 'M'),
        Job(2024, 'EN', 'FT', 'AI Engineer', 150000, 'USD', 150000, 'US', 50, 'US', 'S')
    ])
    def test_plot_jobs_by_experience_level(self, mock_get_jobs, mock_show):
        try:
            JobDataVisualizer.plot_jobs_by_experience_level()
        except Exception:
            self.fail("plot_jobs_by_experience_level() raised Exception unexpectedly!")

    @patch('job_data_visualizer.plt.show')
    @patch('job_data_reader.JobDataReader.get_jobs', return_value=[
        Job(2024, 'SE', 'FT', 'Data Engineer', 100000, 'USD', 100000, 'US', 100, 'US', 'L'),
        Job(2024, 'MI', 'PT', 'Data Scientist', 120000, 'USD', 120000, 'US', 0, 'US', 'M'),
        Job(2024, 'EN', 'FT', 'AI Engineer', 150000, 'USD', 150000, 'US', 50, 'US', 'S')
    ])
    def test_plot_average_salary_by_job_title(self, mock_get_jobs, mock_show):
        try:
            JobDataVisualizer.plot_average_salary_by_job_title('Data Engineer')
        except Exception:
            self.fail("plot_average_salary_by_job_title() raised Exception unexpectedly!")

    @patch('job_data_visualizer.plt.show')
    @patch('job_data_reader.JobDataReader.get_jobs', return_value=[
        Job(2024, 'SE', 'FT', 'Data Engineer', 100000, 'USD', 100000, 'US', 100, 'US', 'L'),
        Job(2024, 'MI', 'PT', 'Data Scientist', 120000, 'USD', 120000, 'US', 0, 'US', 'M'),
        Job(2024, 'EN', 'FT', 'AI Engineer', 150000, 'USD', 150000, 'US', 50, 'US', 'S')
    ])
    def test_plot_average_salary_by_experience_level(self, mock_get_jobs, mock_show):
        try:
            JobDataVisualizer.plot_average_salary_by_experience_level()
        except Exception:
            self.fail("plot_average_salary_by_experience_level() raised Exception unexpectedly!")

    @patch('job_data_visualizer.plt.show')
    @patch('job_data_reader.JobDataReader.get_jobs', return_value=[
        Job(2024, 'SE', 'FT', 'Data Engineer', 100000, 'USD', 100000, 'US', 100, 'US', 'L'),
        Job(2024, 'MI', 'PT', 'Data Scientist', 120000, 'USD', 120000, 'US', 0, 'US', 'M'),
        Job(2024, 'EN', 'FT', 'AI Engineer', 150000, 'USD', 150000, 'US', 50, 'US', 'S')
    ])
    def test_plot_jobs_by_employment_type(self, mock_get_jobs, mock_show):
        try:
            JobDataVisualizer.plot_jobs_by_employment_type()
        except Exception:
            self.fail("plot_jobs_by_employment_type() raised Exception unexpectedly!")

    @patch('job_data_visualizer.plt.show')
    @patch('job_data_reader.JobDataReader.get_jobs', return_value=[
        Job(2024, 'SE', 'FT', 'Data Engineer', 100000, 'USD', 100000, 'US', 100, 'US', 'L'),
        Job(2024, 'MI', 'PT', 'Data Scientist', 120000, 'USD', 120000, 'US', 0, 'US', 'M'),
        Job(2024, 'EN', 'FT', 'AI Engineer', 150000, 'USD', 150000, 'US', 50, 'US', 'S')
    ])
    def test_plot_remote_jobs_ratio(self, mock_get_jobs, mock_show):
        try:
            JobDataVisualizer.plot_remote_jobs_ratio()
        except Exception:
            self.fail("plot_remote_jobs_ratio() raised Exception unexpectedly!")

if __name__ == '__main__':
    unittest.main()
