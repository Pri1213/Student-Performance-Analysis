import unittest
from unittest.mock import MagicMock
from controller.underperformingStudent import identify_underperforming_students

class TestUnderperformingStudents(unittest.TestCase):
    def setUp(self):
        # Mocking the database connection and cursor
        self.conn = MagicMock()
        self.cursor = MagicMock()
        self.conn.cursor.return_value = self.cursor

    def tearDown(self):
        pass

    def test_identify_underperforming_students(self):
        # Mocking the SQL query result
        expected_result = [
            (1, 'Mock_Test', 60, 240),
            (1, 'Formative_Test_1', 55, 240),
            (2, 'Mock_Test', 65, 250),
            (2, 'Formative_Test_1', 50, 250),
        ]
        self.cursor.fetchall.return_value = expected_result

        # Calling the function under test
        result = identify_underperforming_students()

        # Asserting the result
        self.assertEqual(result, expected_result)

        # Asserting the database connection and cursor calls
        self.conn.cursor.assert_called_once()
        self.cursor.execute.assert_called_once_with("""
        WITH AllFormativeTests AS (
          SELECT researchid, Grade, 'Mock_Test' AS TestName FROM Mock_Test
          UNION ALL
          SELECT researchid, Grade, 'Formative_Test_1' AS TestName FROM Formative_Test_1
          UNION ALL
          SELECT researchid, Grade, 'Formative_Test_2' AS TestName FROM Formative_Test_2
          UNION ALL
          SELECT researchid, Grade, 'Formative_Test_3' AS TestName FROM Formative_Test_3
          UNION ALL
          SELECT researchid, Grade, 'Formative_Test_4' AS TestName FROM Formative_Test_4
        )

        SELECT aft.researchid, aft.TestName, aft.Grade AS FormativeTestGrade, st.Grade AS SumTestGrade
        FROM AllFormativeTests aft
        JOIN SumTest st ON aft.researchid = st.researchid
        WHERE aft.researchid IN (
          SELECT researchid
          FROM AllFormativeTests
          GROUP BY researchid
          HAVING AVG(Grade) < (SELECT AVG(Grade) FROM AllFormativeTests)
        )
        ORDER BY aft.researchid, aft.TestName, aft.Grade
        LIMIT 50;
        """)

        self.cursor.fetchall.assert_called_once()

if __name__ == '__main__':
    unittest.main()