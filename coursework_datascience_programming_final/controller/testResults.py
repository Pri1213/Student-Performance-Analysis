#Author: F332321
import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def retrieve_test_scores_for_student(student_id):
    """
    Retrieves the test scores for a given student ID from a SQLite database.
    
    Parameters:
    - student_id (int): The ID of the student
    
    Returns:
    - test_scores (list): A list of dictionaries containing the table name and grade for each test
    """
    notebook_dir = os.getcwd()

    db_relative_path = os.path.join(notebook_dir, '..', 'data', 'ResultsDatabase.db')

    db_path = os.path.abspath(db_relative_path)
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    tables_to_query = ['Mock_Test', 'Formative_Test_1', 'Formative_Test_2', 'Formative_Test_3', 'Formative_Test_4', 'SumTest']

    test_scores = []

    for table in tables_to_query:
        cursor.execute(f"PRAGMA table_info({table})")
        if cursor.fetchall():
            query = f"SELECT Grade FROM {table} WHERE researchid = ?"
            cursor.execute(query, (student_id,))
            
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            
            for row in rows:
                test_scores.append({'Table': table, 'Grade': row[0]})

    conn.close()

    return test_scores

def visualize_test_scores(test_scores, student_id):
    """
    Visualizes the test scores for a given student ID using a bar chart.
    
    Parameters:
    - test_scores (list): A list of dictionaries containing the table name and grade for each test
    - student_id (int): The ID of the student
    
    Returns:
    - None
    """
    table_names = [score['Table'] for score in test_scores]
    grades = [score['Grade'] for score in test_scores]

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(table_names, grades, color='skyblue')
    ax.set_title(f'Test Scores for Student {student_id}')
    ax.set_xlabel('Table')
    ax.set_ylabel('Grade')
    ax.set_ylim(0, 110) 

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

    plt.show()

    plt.close(fig)

def main():
    student_id = int(input("Enter the student ID: "))
    test_scores = retrieve_test_scores_for_student(student_id)
    
    visualize_test_scores(test_scores, student_id)
    
    return test_scores, student_id

if __name__ == "__main__":
    main()
