# Author: F332321

import sqlite3
import os

def connect_to_database():
    """
    Connects to the SQLite database.

    Returns:
    conn (sqlite3.Connection): The database connection object.
    """
    notebook_dir = os.getcwd()

    db_relative_path = os.path.join(notebook_dir, '..', 'data', 'ResultsDatabase.db')


    db_path = os.path.abspath(db_relative_path)
    conn = sqlite3.connect(db_path)
    return conn

def disconnect_from_database(conn):
    """
    Disconnects from the database.

    Args:
    conn (sqlite3.Connection): The database connection object.
    """
    conn.close()

def execute_query(conn, sql_query):
    """
    Executes a SQL query on the database.

    Args:
    conn (sqlite3.Connection): The database connection object.
    sql_query (str): The SQL query to execute.

    Returns:
    results (list): The results of the query.
    """
    cursor = conn.cursor()
    # Execute the query
    cursor.execute(sql_query)

    # Fetch the results
    results = cursor.fetchall()
    return results

def identify_hardworking_students():
    """
    Identifies the hardworking students based on their grades.

    This function executes an SQL query to retrieve the research IDs, programming levels, and grades of students 
    who have performed better than the average grade for their respective programming level 
    in all tests (Formative_Test_1, Mock_Test, SumTest, Formative_Test_2, Formative_Test_3, Formative_Test_4). 
    The query joins multiple tables and calculates the average grade for each programming level 
    using a common table expression (CTE) called StudentAverages. 
    The query then filters the results to include only the students whose grades are higher 
    than the average grade for their programming level in all tests. The results are sorted by programming level.

    Returns:
    results (list): The list of hardworking students and their grades.
    """
    conn = connect_to_database()

    sql_query = """
       WITH StudentAverages AS (
    SELECT
        Programming_Level,
        AVG(Grade) AS AverageGrade
    FROM (
        SELECT researchid, Grade FROM Formative_Test_1
        UNION ALL
        SELECT researchid, Grade FROM Mock_Test
        UNION ALL
        SELECT researchid, Grade FROM SumTest
        UNION ALL
        SELECT researchid, Grade FROM Formative_Test_2
        UNION ALL
        SELECT researchid, Grade FROM Formative_Test_3
        UNION ALL
        SELECT researchid, Grade FROM Formative_Test_4
    ) AS AllTests
    INNER JOIN StudentRate ON AllTests.researchid = StudentRate.researchid
    GROUP BY Programming_Level
)

    SELECT
        sr.researchid,
        sr.Programming_Level,
        mt.Grade AS Mock_Test_Grade,
        st.Grade AS SumTest_Grade,
        ft1.Grade AS Formative_Test_1_Grade,
        ft2.Grade AS Formative_Test_2_Grade,
        ft3.Grade AS Formative_Test_3_Grade,
        ft4.Grade AS Formative_Test_4_Grade
    FROM
        StudentRate sr
        JOIN Formative_Test_1 ft1 ON sr.researchid = ft1.researchid
        JOIN Mock_Test mt ON sr.researchid = mt.researchid
        JOIN SumTest st ON sr.researchid = st.researchid
        JOIN Formative_Test_2 ft2 ON sr.researchid = ft2.researchid
        JOIN Formative_Test_3 ft3 ON sr.researchid = ft3.researchid
        JOIN Formative_Test_4 ft4 ON sr.researchid = ft4.researchid
        JOIN StudentAverages sa ON sr.Programming_Level = sa.Programming_Level
    WHERE
        ft1.Grade > sa.AverageGrade
        AND mt.Grade > sa.AverageGrade
        AND st.Grade > sa.AverageGrade
        AND ft2.Grade > sa.AverageGrade
        AND ft3.Grade > sa.AverageGrade
        AND ft4.Grade > sa.AverageGrade
    ORDER BY
        sr.Programming_Level;

    """

    results = execute_query(conn, sql_query)

    disconnect_from_database(conn)

    return results

results = identify_hardworking_students()
results.sort(key=lambda row: row[0])  


def main():
    # Connect to the database
    conn = connect_to_database()

    # Identify hardworking students
    results = identify_hardworking_students()
    results.sort(key=lambda row: row[0])

    # Disconnect from the database
    disconnect_from_database(conn)

    # Print the list of hardworking students
    print(results)

if __name__ == "__main__":
    main()
