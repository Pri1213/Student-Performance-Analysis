import unittest
from unittest.mock import patch

from controller.hardworkingStudents import identify_hardworking_students

class TestHardworkingStudents(unittest.TestCase):
    def test_identify_hardworking_students(self, mock_connect, mock_execute_query, mock_disconnect):
        # Mock the return value of execute_query
        mock_execute_query.return_value = [
            (1, 'Beginner', 80, 90, 85, 95, 88, 92),
            (2, 'Intermediate', 75, 85, 80, 90, 82, 88)
        ]

        # Call the function
        result = identify_hardworking_students()

        # Assert the expected result
        expected_result = [
            (1, 'Beginner', 80, 90, 85, 95, 88, 92),
            (2, 'Intermediate', 75, 85, 80, 90, 82, 88)
        ]
        self.assertEqual(result, expected_result)

        # Assert that the necessary functions were called
        mock_connect.assert_called_once()
        mock_execute_query.assert_called_once()
        mock_disconnect.assert_called_once()

if __name__ == "__main__":
    unittest.main()