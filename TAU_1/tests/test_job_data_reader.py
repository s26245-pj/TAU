import unittest
from unittest.mock import patch, MagicMock
from job_data_reader import JobDataReader, Job

class TestJobDataReader(unittest.TestCase):

    def setUp(self):
        self.reader = JobDataReader()
        self.reader.read('../data.csv')  # Assuming you have a test CSV file

    def test_read_jobs(self):
        jobs = self.reader.get_jobs()
        self.assertIsInstance(jobs, list)
        self.assertGreater(len(jobs), 0)
        self.assertIsInstance(jobs[0], Job)

    def test_missing_file(self):
        reader = JobDataReader()
        with self.assertRaises(FileNotFoundError):
            reader.read('missing_file.csv')

    @patch('pandas.read_csv')
    def test_missing_column(self, mock_read_csv):
        # Mock the DataFrame returned by pandas.read_csv to simulate missing columns
        mock_df = MagicMock()
        mock_df.iterrows.return_value = iter([(0, {
            'work_year': 2024,
            'experience_level': 'SE',
            'employment_type': 'FT',
            'job_title': 'Data Engineer',
            # Intentionally omit 'salary', 'salary_currency', etc.
        })])
        mock_read_csv.return_value = mock_df

        reader = JobDataReader()
        with self.assertRaises(KeyError):
            reader.read('test_missing_column.csv')

if __name__ == '__main__':
    unittest.main()
