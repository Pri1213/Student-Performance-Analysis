#Author: F332321
import sqlite3
import os
import pandas as pd

def connect_to_database():
    notebook_dir = os.getcwd()
    db_relative_path = os.path.join(notebook_dir, '..', 'data', 'ResultsDatabase.db')
    db_path = os.path.abspath(db_relative_path)
    
    conn = sqlite3.connect(db_path)
    return conn

def disconnect_from_database(conn):
    conn.close()

def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


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