#Author: F332321

import statistics
import os
import sqlite3
import numpy as np
import matplotlib.pyplot as plt  
import math


def retrieve_all_grades(table_to_retrieve):
    """
    Retrieves all grades from a specified table in the ResultsDatabase.db.

    Parameters:
    - table_to_retrieve (str): The name of the table to retrieve grades from.

    Returns:
    - all_grades (list): A list of all grades retrieved from the table.
    """
    
    notebook_dir = os.getcwd()

    db_relative_path = os.path.join(notebook_dir, '..', 'data', 'ResultsDatabase.db')

    db_path = os.path.abspath(db_relative_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query_all = f"SELECT Grade FROM {table_to_retrieve}"
    cursor.execute(query_all)
    all_results = cursor.fetchall()

    all_grades = [result[0] for result in all_results]

    conn.close()

    return all_grades

def retrieve_scores_for_student(student_id_to_retrieve, table_to_retrieve):
    """
    Retrieves the individual scores for a given student ID from a specified table in the ResultsDatabase.db.

    Parameters:
    - student_id_to_retrieve (int): The ID of the student to retrieve scores for.
    - table_to_retrieve (str): The name of the table to retrieve scores from.

    Returns:
    - scores_for_student (list): A list of individual scores for the given student ID.
    """
    notebook_dir = os.getcwd()

    db_relative_path = os.path.join(notebook_dir, '..', 'data', 'ResultsDatabase.db')

    db_path = os.path.abspath(db_relative_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query_individual = f"SELECT Grade FROM {table_to_retrieve} WHERE researchid = ?"
    cursor.execute(query_individual, (student_id_to_retrieve,))
    scores_for_student = cursor.fetchall()
    conn.close()

    return scores_for_student

def calculate_test_average(all_grades):
    """
    Calculates the average test grade from a list of grades.

    Parameters:
    - all_grades (list): A list of grades.

    Returns:
    - test_average (float): The average test grade.
    """
    return statistics.mean(all_grades)

def calculate_standard_deviation(all_grades):
    """
    Calculates the standard deviation of test grades from a list of grades.

    Parameters:
    - all_grades (list): A list of grades.

    Returns:
    - standard_deviation (float): The standard deviation of test grades.
    """
    
    return statistics.stdev(all_grades)

def calculate_z_score(score_for_student, test_average, standard_deviation):
    """
    Calculates the z-score for a given student's score, test average, and standard deviation.

    Parameters:
    - score_for_student (float): The score of the student.
    - test_average (float): The average test grade.
    - standard_deviation (float): The standard deviation of test grades.

    Returns:
    - z_score (float): The z-score of the student's score.
    """
    
    return (score_for_student - test_average) / standard_deviation

def determine_performance_category(z_score):
    """
    Determines the performance category based on the z-score.

    Parameters:
    - z_score (float): The z-score of the student's score.

    Returns:
    - performance_category (str): The performance category ('Above Mean', 'Below Mean', or 'Equal to Mean').
    """
    
    if z_score > 0:
        return "Above Mean"
    elif z_score < 0:
        return "Below Mean"
    else:
        return "Equal to Mean"

def plot_test_grades_distribution(all_grades, score_for_student, test_average):
    """
    Plots the distribution of test grades and highlights the individual and mean grades.

    Parameters:
    - all_grades (list): A list of all grades.
    - score_for_student (float): The score of the student.
    - test_average (float): The average test grade.

    Returns:
    - None
    """
    plt.figure(figsize=(8, 6))

    plt.hist(all_grades, bins=10, color='skyblue', edgecolor='black')


    plt.xlabel('Grades')
    plt.ylabel('Frequency')
    plt.title('Distribution of Test Grades')

    plt.axvline(x=score_for_student, color='yellow', linestyle='--', label='Individual Grade')

    plt.axvline(x=test_average, color='purple', linestyle='--', label='Mean Grade')

    plt.text(score_for_student, plt.ylim()[1], f'Individual Grade: {score_for_student}', color='yellow', ha='right', va='bottom')
    plt.text(test_average, plt.ylim()[1], f'Mean Grade: {test_average:.2f}', color='purple', ha='right', va='bottom')

    plt.grid(True)
    plt.xticks(np.arange(0, 101, 10))
    plt.yticks(np.arange(0, len(all_grades)+1, len(all_grades)//10))

    plt.legend()

    plt.show()
    
def show_student_performance(score_for_student, test_average):
    """
    Displays the relative performance of a student compared to the mean using a bar chart.

    Parameters:
    - score_for_student (float): The score of the student.
    - test_average (float): The average test grade.

    Returns:
    - None
    """
    categories = ['Student', 'Mean']
    scores = [score_for_student, test_average]

    bar_colors = ['steelblue', 'lightcoral']

    plt.bar(categories, scores, color=bar_colors)
    
    plt.axhline(y=test_average, color='gray', linestyle='--', linewidth=1, label='Mean')

    for i, score in enumerate(scores):
        plt.text(i, score, f'{score:.2f}', ha='center', va='bottom', color='black', fontsize=10)

    plt.title("Relative Performance Comparison")
    plt.ylabel("Test Score")
    plt.legend()
    plt.show()


def view_overall_test_absolute_and_relative_performance(table_to_retrieve,student_id_to_retrieve):
    """
    Retrieves test grades and calculates absolute and relative performance for a given student.

    Parameters:
    - table_to_retrieve (str): The name of the table to retrieve grades from.
    - student_id_to_retrieve (int): The ID of the student to retrieve scores for.

    Returns:
    - None
    """

    all_grades = retrieve_all_grades(table_to_retrieve)
    scores_for_student = retrieve_scores_for_student(student_id_to_retrieve, table_to_retrieve)

    if not scores_for_student:
        print("No test scores found for the given student.")
        return

    score_for_student = scores_for_student[0][0]
    test_average = calculate_test_average(all_grades)
    standard_deviation = calculate_standard_deviation(all_grades)
    z_score = calculate_z_score(score_for_student, test_average, standard_deviation)
    performance_category = determine_performance_category(z_score)

    categories = ['Student', 'Mean']
    scores = [score_for_student, test_average]

    bar_colors = ['steelblue', 'lightcoral']

    plt.bar(categories, scores, color=bar_colors)
    
    plt.axhline(y=test_average, color='gray', linestyle='--', linewidth=1, label='Mean')

    for i, score in enumerate(scores):
        plt.text(i, score, f'{score:.2f}', ha='center', va='bottom', color='black', fontsize=10)

    plt.title("Relative Performance Comparison")
    plt.ylabel("Test Score")
    plt.legend()
    plt.show()



    
def display_overall_test_absolute_and_relative_performance(student_id_to_retrieve, table_to_retrieve):
    """
    Retrieves test grades and calculates absolute and relative performance for a given student, and displays the result.

    Parameters:
    - student_id_to_retrieve (int): The ID of the student to retrieve scores for.
    - table_to_retrieve (str): The name of the table to retrieve grades from.

    Returns:
    - None
    """
    all_grades = retrieve_all_grades(table_to_retrieve)
    scores_for_student = retrieve_scores_for_student(student_id_to_retrieve, table_to_retrieve)

    if not scores_for_student:
        print("No test scores found for the given student.")
        return
    score_for_student = scores_for_student[0][0]

    test_average = calculate_test_average(all_grades)
    standard_deviation = calculate_standard_deviation(all_grades)
    z_score = calculate_z_score(score_for_student, test_average, standard_deviation)
    performance_category = determine_performance_category(z_score)

    print(f"Student ID: {student_id_to_retrieve}, Table: {table_to_retrieve}, Absolute Performance: {score_for_student}, Performance Category: {performance_category}, Relative Performance: {z_score:.2f}")


def visualize_z_score_on_bell_curve(student_id_to_retrieve, table_to_retrieve):
    
    """
    Retrieves test grades, calculates the z-score for a given student, and visualizes the z-score on a bell curve.

    Parameters:
    - student_id_to_retrieve (int): The ID of the student to retrieve scores for.
    - table_to_retrieve (str): The name of the table to retrieve grades from.

    Returns:
    - None
    """
    scores_for_student = retrieve_scores_for_student(student_id_to_retrieve, table_to_retrieve)
    all_grades = retrieve_all_grades(table_to_retrieve)

    if not scores_for_student:
        print("No test scores found for the given student.")
        return

   
    score_for_student = scores_for_student[0][0]
    test_average = calculate_test_average(all_grades)
    standard_deviation = calculate_standard_deviation(all_grades)
    z_score = calculate_z_score(score_for_student, test_average, standard_deviation)

    
    x = [test_average + i * (standard_deviation / 10) for i in range(-30, 31)]

    
    pdf_values = [1 / (standard_deviation * math.sqrt(2 * math.pi)) * 
                  math.exp(-((xi - test_average) / standard_deviation) ** 2 / 2) for xi in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf_values, label='Standard Deviation Bell Curve')
 
    plt.axvline(x=test_average, color='lightgreen', linestyle='--', linewidth=1, label='Mean')
    plt.text(test_average, 0.01, f'Mean: {test_average:.2f}', color='green', fontsize=6, rotation=90)
    
    plt.axvline(x=score_for_student, color='lightpink', linestyle='--', linewidth=1, label='Student Score')
    plt.text(score_for_student, 0.01, f'Student Score: {score_for_student:.2f}', color='red', fontsize=6, rotation=90)
   
    plt.title("Student Overall Performance")
    plt.legend()
    plt.show()


def main():
    try:
        table_to_retrieve = input("Enter the name of the table to retrieve grades from: ")
        if not table_to_retrieve:
            raise ValueError("Table name cannot be empty.")

        student_id_to_retrieve = int(input("Enter the ID of the student to retrieve scores for: "))

        display_overall_test_absolute_and_relative_performance(student_id_to_retrieve, table_to_retrieve)

        # Visualize the z-score on a bell curve
        visualize_z_score_on_bell_curve(student_id_to_retrieve, table_to_retrieve)
    except ValueError as ve:
        print(f"Invalid input: {str(ve)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
