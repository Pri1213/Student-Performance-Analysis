#Author: F332321
import sqlite3
import os


def identify_underperforming_students():
    """
    Retrieves a list of underperforming students based on their formative test grades.

    Returns:
        A list of tuples containing the research ID, test name, formative test grade, and sum test grade
        for each underperforming student.
    Logic:   
    The provided SQL query is used to retrieve information about underperforming students based on their grades in formative tests. Let's break down the query step by step:
    The query starts with a Common Table Expression (CTE) named "AllFormativeTests". 
    CTEs are temporary result sets that can be referenced within the main query. In this CTE, 
    multiple SELECT statements are combined using the UNION ALL operator to fetch data from different tables 
    representing different formative tests (Mock_Test, Formative_Test_1, Formative_Test_2, Formative_Test_3, and Formative_Test_4). 
    The result of this CTE will have columns: researchid, Grade, and TestName.The main query then selects columns from the "AllFormativeTests" CTE 
    and joins it with another table called "SumTest" using the researchid column. The "SumTest" table likely contains the cumulative grades of all tests 
    for each student. The selected columns are: researchid, TestName, FormativeTestGrade (Grade from the "AllFormativeTests" CTE), and 
    SumTestGrade (Grade from the "SumTest" table).
    The WHERE clause filters the result set by selecting only those researchids that meet a certain condition. 
    The condition is that the researchid must be present in a subquery that calculates the average grade for each researchid in 
    the "AllFormativeTests" CTE and compares it with the overall average grade of all students in the "AllFormativeTests" CTE. 
    This condition ensures that only the researchids of students with below-average formative test grades are included in the result set.
    The result set is then ordered by researchid, TestName, and Grade in ascending order.
    Finally, the LIMIT clause is used to restrict the result set to a maximum of 50 rows.
    """
    notebook_dir = os.getcwd()

    db_relative_path = os.path.join(notebook_dir, '..', 'data', 'ResultsDatabase.db')

    db_path = os.path.abspath(db_relative_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    sql_query = """
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
    """

    cursor.execute(sql_query)

    results = cursor.fetchall()

    conn.close()

    return results

underperforming_students = identify_underperforming_students()
sorted_results = sorted(underperforming_students, key=lambda x: x[3], reverse=True)

lowest_grades = {}

for row in sorted_results:
    research_id = row[0]
    test_name = row[1]
    formative_test_grade = row[2]
    sum_test_grade = row[3]
    
    if research_id in lowest_grades:
        if formative_test_grade < lowest_grades[research_id]:
            lowest_grades[research_id] = formative_test_grade
    else:
        lowest_grades[research_id] = formative_test_grade
    
def main():
  underperforming_students = identify_underperforming_students()
  sorted_results = sorted(underperforming_students, key=lambda x: x[3], reverse=True)

  lowest_grades = {}

  for row in sorted_results:
    research_id = row[0]
    test_name = row[1]
    formative_test_grade = row[2]
    sum_test_grade = row[3]

    if research_id in lowest_grades:
      if formative_test_grade < lowest_grades[research_id]:
        lowest_grades[research_id] = formative_test_grade
    else:
      lowest_grades[research_id] = formative_test_grade

  lowest_grades_list = list(lowest_grades.items())
  print(lowest_grades_list)


if __name__ == "__main__":
  main()




    


