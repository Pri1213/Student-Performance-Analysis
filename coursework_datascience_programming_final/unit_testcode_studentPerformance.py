#Author: F332321

import unittest
from unittest.mock import patch
from controller.studentPerformance import *

class TestPerformanceAnalysis(unittest.TestCase):

    def setUp(self):
        self.db_path = ':memory:'
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        tables_to_query = ['Mock_Test', 'Formative_Test_1', 'Formative_Test_2', 'Formative_Test_3', 'Formative_Test_4', 'SumTest']

        for table in tables_to_query:
            cursor.execute(f"CREATE TABLE {table} (researchid INT, Grade INT)")
            cursor.execute(f"INSERT INTO {table} (researchid, Grade) VALUES (?, ?)", (123, 80)) 

        conn.commit()
        conn.close()

    def tearDown(self):
        # Clean up by removing the temporary database
        del self.db_path

    def test_retrieve_all_grades(self):
        # Provide a known table name for testing
        table_to_retrieve = 'Mock_Test'

        # Call the function to retrieve all grades
        all_grades = retrieve_all_grades(table_to_retrieve)

        # Check if the returned value is a list
        self.assertIsInstance(all_grades, list)

        # Check if the length of the returned list is correct
        self.assertEqual(len(all_grades), 1)

        # Check if the grade in the list is correct
        self.assertEqual(all_grades[0], 80)

    def test_retrieve_scores_for_student(self):
        # Provide a known student ID and table name for testing
        student_id_to_retrieve = 123
        table_to_retrieve = 'Mock_Test'

        # Call the function to retrieve scores for the student
        scores_for_student = retrieve_scores_for_student(student_id_to_retrieve, table_to_retrieve)

        # Check if the returned value is a list
        self.assertIsInstance(scores_for_student, list)

        # Check if the length of the returned list is correct
        self.assertEqual(len(scores_for_student), 1)

        # Check if the score in the list is correct
        self.assertEqual(scores_for_student[0][0], 80)

    def test_calculate_test_average(self):
        # Provide a list of grades for testing
        all_grades = [80, 90, 75, 85, 95]

        # Call the function to calculate the test average
        test_average = calculate_test_average(all_grades)

        # Check if the returned value is a float
        self.assertIsInstance(test_average, float)

        # Check if the calculated test average is correct
        self.assertEqual(test_average, 85)

    def test_calculate_standard_deviation(self):
        # Provide a list of grades for testing
        all_grades = [80, 90, 75, 85, 95]

        # Call the function to calculate the standard deviation
        standard_deviation = calculate_standard_deviation(all_grades)

        # Check if the returned value is a float
        self.assertIsInstance(standard_deviation, float)

        # Check if the calculated standard deviation is correct
        self.assertAlmostEqual(standard_deviation, 7.905694150420948)

    def test_calculate_z_score(self):
        # Provide a known score, test average, and standard deviation for testing
        score_for_student = 80
        test_average = 85
        standard_deviation = 7.905694150420948

        # Call the function to calculate the z-score
        z_score = calculate_z_score(score_for_student, test_average, standard_deviation)

        # Check if the returned value is a float
        self.assertIsInstance(z_score, float)

        # Check if the calculated z-score is correct
        self.assertAlmostEqual(z_score, -0.6324555320336759)

    def test_determine_performance_category(self):
        # Provide a known z-score for testing
        z_score = -0.6324555320336759

        # Call the function to determine the performance category
        performance_category = determine_performance_category(z_score)

        # Check if the returned value is a string
        self.assertIsInstance(performance_category, str)

        # Check if the determined performance category is correct
        self.assertEqual(performance_category, "Below Mean")

    @patch('matplotlib.pyplot.show')
    def test_plot_test_grades_distribution(self, mock_show):
        # Provide a list of all grades, an individual score, and the test average for testing
        all_grades = [80, 90, 75, 85, 95]
        score_for_student = 80
        test_average = 85

        # Call the function to plot the test grades distribution
        plot_test_grades_distribution(all_grades, score_for_student, test_average)

        # Check if the show function is called
        mock_show.assert_called_once()

    @patch('matplotlib.pyplot.show')
    def test_show_student_performance(self, mock_show):
        # Provide an individual score and the test average for testing
        score_for_student = 80
        test_average = 85

        # Call the function to show the student performance
        show_student_performance(score_for_student, test_average)

        # Check if the show function is called
        mock_show.assert_called_once()

    def test_view_overall_test_absolute_and_relative_performance(self):
        # Provide a known table name and student ID for testing
        table_to_retrieve = 'Mock_Test'
        student_id_to_retrieve = 123

        # Call the function to view the overall test absolute and relative performance
        view_overall_test_absolute_and_relative_performance(table_to_retrieve, student_id_to_retrieve)

        # No assertions can be made as the function only contains print statements

    def test_display_overall_test_absolute_and_relative_performance(self):
        # Provide a known table name and student ID for testing
        table_to_retrieve = 'Mock_Test'
        student_id_to_retrieve = 123

        # Call the function to display the overall test absolute and relative performance
        with patch('builtins.print') as mock_print:
            display_overall_test_absolute_and_relative_performance(student_id_to_retrieve, table_to_retrieve)

            # Check if the print function is called with the correct arguments
            mock_print.assert_called_once_with("Student ID: 123, Table: Mock_Test, Absolute Performance: 80, Performance Category: Below Mean, Relative Performance: -0.63")

    @patch('matplotlib.pyplot.show')
    def test_visualize_z_score_on_bell_curve(self, mock_show):
        # Provide a known table name and student ID for testing
        table_to_retrieve = 'Mock_Test'
        student_id_to_retrieve = 123

        # Call the function to visualize the z-score on a bell curve
        visualize_z_score_on_bell_curve(student_id_to_retrieve, table_to_retrieve)

        # Check if the show function is called
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()