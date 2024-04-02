#Author: F332321

import pandas as pd
import sqlite3
import os

def load_and_clean_data_Mock_Test():
    """
    Loads and cleans the data from the Mock Test CSV file.
    Performs various data cleaning operations such as renaming columns, replacing values, 
    handling missing values, and converting data types.
    Returns the cleaned DataFrame.
    """
    dfMock_Test = pd.read_csv('data/TestResults Folder/Formative_Mock_Test.csv')
    dfClean_Mock_Test = dfMock_Test.copy()
    dfClean_Mock_Test.columns = dfClean_Mock_Test.columns.str.replace(' ', '').str.replace('/', '')
    dfClean_Mock_Test.columns = dfClean_Mock_Test.columns.str.replace('Q ', 'Q').str.replace(' /', '')
    dfClean_Mock_Test.columns = dfClean_Mock_Test.columns.str.replace('Q1500', 'Q1').str.replace('Q2300', 'Q2').str.replace('Q3600', 'Q3').str.replace('Q4700', 'Q4').str.replace('Q5500', 'Q5').str.replace('Q6400', 'Q6').str.replace('Q71000', 'Q7').str.replace('Q82000', 'Q8').str.replace('Q92000', 'Q9').str.replace('Q102000', 'Q10')
    dfClean_Mock_Test.fillna(0, inplace=True)
    dfClean_Mock_Test.rename(columns={'Grade10000': 'Grade'}, inplace=True)
    dfClean_Mock_Test['Startedon'] = pd.to_datetime(dfClean_Mock_Test['Startedon'])
    dfClean_Mock_Test['Completed'] = pd.to_datetime(dfClean_Mock_Test['Completed'])
    dfClean_Mock_Test.drop('State', axis=1, inplace=True)
    dfClean_Mock_Test.drop('Timetaken', axis=1, inplace=True)
    dfClean_Mock_Test = dfClean_Mock_Test.groupby('researchid').max().reset_index()
    return dfClean_Mock_Test


def load_and_clean_data_Formative_Test_1():
    """
    Loads and cleans the data from the Formative Test 1 CSV file.
    Performs various data cleaning operations such as renaming columns, replacing values, 
    handling missing values, and converting data types.
    Returns the cleaned DataFrame.
    """
    dfTest_1 = pd.read_csv('data/TestResults Folder/Formative_Test_1.csv')
    df_clean_1 = dfTest_1.copy()
    df_clean_1.columns = df_clean_1.columns.str.replace(' ', '').str.replace('/', '')
    df_clean_1.columns = df_clean_1.columns.str.replace('Q ', 'Q').str.replace(' /', '')
    df_clean_1.columns = df_clean_1.columns.str.replace('Q1100', 'Q1').str.replace('Q2100', 'Q2').str.replace('Q3100', 'Q3').str.replace('Q4100', 'Q4').str.replace('Q5100', 'Q5').str.replace('Q6100', 'Q6')
    df_clean_1.fillna(0, inplace=True)
    df_clean_1 = df_clean_1.replace('-', 0)
    df_clean_1.rename(columns={'Grade600': 'Grade'}, inplace=True)
    df_clean_1 = df_clean_1[df_clean_1['Completed'].notnull() & (df_clean_1['Completed'] != 0)]
    df_clean_1['Startedon'] = pd.to_datetime(df_clean_1['Startedon'])
    df_clean_1['Completed'] = pd.to_datetime(df_clean_1['Completed'], errors='coerce')
    df_clean_1.drop('State', axis=1, inplace=True)
    df_clean_1.drop('Timetaken', axis=1, inplace=True)
    df_clean_1['Grade'] = pd.to_numeric(df_clean_1['Grade'], errors='coerce')
    df_clean_1['Grade'] = df_clean_1['Grade'].replace('-', 0)
    df_clean_1['Grade'] = round((df_clean_1['Grade'] / 6) * 100, 2)
    df_formatted_Clean_Test_1 = df_clean_1.copy()
     # Keep only the rows with the highest grade for each unique researchid
    df_formatted_Clean_Test_1 = df_clean_1.loc[df_clean_1.groupby('researchid')['Grade'].idxmax()]
    return df_formatted_Clean_Test_1


def load_and_clean_data_Formative_Test_2():
    """
    Loads and cleans the data from the Formative Test 2 CSV file.
    Performs various data cleaning operations such as renaming columns, replacing values, 
    handling missing values, and converting data types.
    Returns the cleaned DataFrame.
    """
    dfTest_2 = pd.read_csv('data/TestResults Folder/Formative_Test_2.csv')
    df_clean_2 = dfTest_2.copy()
    df_clean_2.columns = df_clean_2.columns.str.replace(' ', '').str.replace('/', '')
    df_clean_2.columns = df_clean_2.columns.str.replace('Q ', 'Q').str.replace(' /', '')
    df_clean_2.columns = df_clean_2.columns.str.replace('Q1100', 'Q1').str.replace('Q2100', 'Q2').str.replace('Q3100', 'Q3').str.replace('Q4200', 'Q4').str.replace('Q5100', 'Q5').str.replace('Q6100', 'Q6')
    df_clean_2.fillna(0, inplace=True)
    df_clean_2 = df_clean_2.replace('-', 0)
    df_clean_2.rename(columns={'Grade700': 'Grade'}, inplace=True)
    df_clean_2 = df_clean_2[df_clean_2['Completed'].notnull() & (df_clean_2['Completed'] != 0)]
    df_clean_2['Startedon'] = pd.to_datetime(df_clean_2['Startedon'])
    df_clean_2['Completed'] = pd.to_datetime(df_clean_2['Completed'], errors='coerce')
    df_clean_2.drop('State', axis=1, inplace=True)
    df_clean_2.drop('Timetaken', axis=1, inplace=True)
    df_clean_2 = df_clean_2.groupby('researchid').max().reset_index()
    df_clean_2['Grade'] = pd.to_numeric(df_clean_2['Grade'], errors='coerce')
    df_clean_2['Grade'] = df_clean_2['Grade'].replace('-', 0)
    df_clean_2['Grade'] = round((df_clean_2['Grade'] / 7) * 100, 2)
    df_formatted_Clean_Test_2 = df_clean_2.copy()
    return df_formatted_Clean_Test_2


def load_and_clean_data_Formative_Test_3():
    """
    Loads and cleans the data from the Formative Test 3 CSV file.
    Performs various data cleaning operations such as renaming columns, replacing values, 
    handling missing values, and converting data types.
    Returns the cleaned DataFrame.
    """
    dfTest_3 = pd.read_csv('data/TestResults Folder/Formative_Test_3.csv')
    df_clean_3 = dfTest_3.copy()
    df_clean_3.columns = df_clean_3.columns.str.replace(' ', '').str.replace('/', '')
    df_clean_3.columns = df_clean_3.columns.str.replace('Q ', 'Q').str.replace(' /', '')
    df_clean_3.columns = df_clean_3.columns.str.replace('Q1100', 'Q1').str.replace('Q2100', 'Q2').str.replace('Q3100', 'Q3').str.replace('Q4100', 'Q4').str.replace('Q5100', 'Q5').str.replace('Q6100', 'Q6')
    df_clean_3.fillna(0, inplace=True)
    df_clean_3 = df_clean_3.replace('-', 0)
    df_clean_3.rename(columns={'Grade600': 'Grade'}, inplace=True)
    df_clean_3 = df_clean_3[df_clean_3['Completed'].notnull() & (df_clean_3['Completed'] != 0)]
    df_clean_3['Startedon'] = pd.to_datetime(df_clean_3['Startedon'])
    df_clean_3['Completed'] = pd.to_datetime(df_clean_3['Completed'], errors='coerce')
    df_clean_3.drop('State', axis=1, inplace=True)
    df_clean_3.drop('Timetaken', axis=1, inplace=True)
    df_clean_3 = df_clean_3.groupby('researchid').max().reset_index()
    df_clean_3['Grade'] = pd.to_numeric(df_clean_3['Grade'], errors='coerce')
    df_clean_3['Grade'] = df_clean_3['Grade'].replace('-', 0)
    df_clean_3['Grade'] = round((df_clean_3['Grade'] / 6) * 100, 2)
    df_formatted_Clean_Test_3 = df_clean_3.copy()
    return df_formatted_Clean_Test_3

def load_and_clean_data_Formative_Test_4():
    """
    Loads and cleans the data from the Formative Test 4 CSV file.
    Performs various data cleaning operations such as renaming columns, replacing values, 
    handling missing values, and converting data types.
    Returns the cleaned DataFrame.
    """
    dfFormative_Test_4 = pd.read_csv('data/TestResults Folder/Formative_Test_4.csv')
    df_clean_4 = dfFormative_Test_4.copy()
    df_clean_4.columns = df_clean_4.columns.str.replace(' ', '').str.replace('/', '')
    df_clean_4.columns = df_clean_4.columns.str.replace('Q ', 'Q').str.replace(' /', '')
    df_clean_4.columns = df_clean_4.columns.str.replace('Q1500', 'Q1').str.replace('Q2500', 'Q2')
    df_clean_4.fillna(0, inplace=True)
    df_clean_4 = df_clean_4.replace('-', 0)
    df_clean_4.rename(columns={'Grade1000': 'Grade'}, inplace=True)
    df_clean_4 = df_clean_4[df_clean_4['Completed'].notnull() & (df_clean_4['Completed'] != 0)]
    df_clean_4['Startedon'] = pd.to_datetime(df_clean_4['Startedon'])
    df_clean_4['Completed'] = pd.to_datetime(df_clean_4['Completed'], errors='coerce')
    df_clean_4.drop('State', axis=1, inplace=True)
    df_clean_4.drop('Timetaken', axis=1, inplace=True)
    df_clean_4 = df_clean_4.groupby('researchid').max().reset_index()
    df_clean_4['Grade'] = pd.to_numeric(df_clean_4['Grade'], errors='coerce')
    df_clean_4['Grade'] = df_clean_4['Grade'].replace('-', 0)
    df_clean_4['Grade'] = round((df_clean_4['Grade'] / 10) * 100, 2)
    df_formatted_Formative_Test_4 = df_clean_4.copy()
    return df_formatted_Formative_Test_4


def load_and_clean_data_StudentRate():
    """
    Loads and cleans the data from the StudentRate CSV file.
    Performs various data cleaning operations such as renaming columns.
    Returns the cleaned DataFrame.
    """
    # Load data from CSV into a DataFrame
    df_StudentRate = pd.read_csv('data/TestResults Folder/StudentRate.csv')

    # Create a copy of the original DataFrame
    df_clean_StudentRate = df_StudentRate.copy()

    # Rename specific columns
    df_clean_StudentRate = df_clean_StudentRate.rename(columns={
        'research id': 'researchid',
        'Which of followings are true for you': 'Background_Knowledge',
        'Which of the followings have you studied or had experience with': 'Experience',
        'What level programming knowledge do you have?': 'Programming_Level',
        'Do you like programming': 'Like_Programming',
        'What do you think about sci-fi movies ?': 'Opinion_SciFi_Movies',
        'What do you think about learning to program  ?': 'Opinion_Learning_Programming',
        'Can you please specify the programming language you know': 'Known_Languages'
    })


    return df_clean_StudentRate


def load_and_clean_data_SumTest():
    """
    Loads and cleans the data from the SumTest CSV file.
    Performs various data cleaning operations such as renaming columns, replacing values, handling missing values, and converting data types.
    Returns the cleaned DataFrame.
    """
    dfSumTest = pd.read_csv('data/TestResults Folder/SumTest.csv')
    df_clean_SumTest = dfSumTest.copy()
    df_clean_SumTest.columns = df_clean_SumTest.columns.str.replace(' ', '').str.replace('/', '')
    df_clean_SumTest.columns = df_clean_SumTest.columns.str.replace('Q ', 'Q').str.replace(' /', '')
    df_clean_SumTest.columns = df_clean_SumTest.columns.str.replace('Q1500', 'Q1').str.replace('Q2300', 'Q2').str.replace('Q3600', 'Q3').str.replace('Q4700', 'Q4').str.replace('Q5400', 'Q5').str.replace('Q6500', 'Q6').str.replace('Q71500', 'Q7').str.replace('Q81500', 'Q8').str.replace('Q91500', 'Q9').str.replace('Q101000', 'Q10').str.replace('Q11400', 'Q11').str.replace('Q12500', 'Q12').str.replace('Q13600', 'Q13')
    df_clean_SumTest.fillna(0, inplace=True)
    df_clean_SumTest = df_clean_SumTest.replace('-', 0)
    df_clean_SumTest.rename(columns={'Grade10000': 'Grade'}, inplace=True)
    df_clean_SumTest = df_clean_SumTest[df_clean_SumTest['Completed'].notnull() & (df_clean_SumTest['Completed'] != 0)]
    df_clean_SumTest['Startedon'] = pd.to_datetime(df_clean_SumTest['Startedon'])
    df_clean_SumTest['Completed'] = pd.to_datetime(df_clean_SumTest['Completed'], errors='coerce')
    df_clean_SumTest.drop('State', axis=1, inplace=True)
    df_clean_SumTest.drop('Timetaken', axis=1, inplace=True)
    df_clean_SumTest = df_clean_SumTest.groupby('researchid').max().reset_index()
    df_clean_SumTest['Grade'] = pd.to_numeric(df_clean_SumTest['Grade'], errors='coerce')
    df_clean_SumTest['Grade'] = df_clean_SumTest['Grade'].replace('-', 0)
    df_formatted_SumTest = df_clean_SumTest.copy()
    return df_formatted_SumTest



def create_database():
    """
    Creates a SQLite database and tables for each cleaned dataset.
    """
    db_path = os.path.join('data', 'ResultsDatabase.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables for each cleaned dataset
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Mock_Test (
        researchid INTEGER PRIMARY KEY,
        Startedon DATETIME,
        Completed DATETIME,
        Q1 INTEGER,
        Q2 INTEGER,
        Q3 INTEGER,
        Q4 INTEGER,
        Q5 INTEGER,
        Q6 INTEGER,
        Q7 INTEGER,
        Q8 INTEGER,
        Q9 INTEGER,
        Q10 INTEGER,
        Grade INTEGER
    );
    
    CREATE TABLE IF NOT EXISTS Formative_Test_1 (
        researchid INTEGER PRIMARY KEY,
        Startedon DATETIME,
        Completed DATETIME,
        Q1 INTEGER,
        Q2 INTEGER,
        Q3 INTEGER,
        Q4 INTEGER,
        Q5 INTEGER,
        Q6 INTEGER,
        Grade INTEGER
    );

    CREATE TABLE IF NOT EXISTS Formative_Test_2 (
        researchid INTEGER PRIMARY KEY,
        Startedon DATETIME,
        Completed DATETIME,
        Q1 INTEGER,
        Q2 INTEGER,
        Q3 INTEGER,
        Q4 INTEGER,
        Q5 INTEGER,
        Q6 INTEGER,
        Grade INTEGER
    );

    CREATE TABLE IF NOT EXISTS Formative_Test_3 (
        researchid INTEGER PRIMARY KEY,
        Startedon DATETIME,
        Completed DATETIME,
        Q1 INTEGER,
        Q2 INTEGER,
        Q3 INTEGER,
        Q4 INTEGER,
        Q5 INTEGER,
        Q6 INTEGER,
        Grade INTEGER
    );

    CREATE TABLE IF NOT EXISTS Formative_Test_4 (
        researchid INTEGER PRIMARY KEY,
        Startedon DATETIME,
        Completed DATETIME,
        Q1 INTEGER,
        Q2 INTEGER,
        Grade INTEGER
    );

    CREATE TABLE IF NOT EXISTS StudentRate (
        researchid INTEGER PRIMARY KEY,
        Background_Knowledge VARCHAR(255),
        Experience VARCHAR(255),
        Programming_Level VARCHAR(255),
        Like_Programming VARCHAR(255),
        Opinion_SciFi_Movies VARCHAR(255),
        Opinion_Learning_Programming VARCHAR(255),
        Known_Languages VARCHAR(255)
    );

    CREATE TABLE IF NOT EXISTS SumTest (
        researchid INTEGER PRIMARY KEY,
        Startedon DATETIME,
        Completed DATETIME,
        Q1 INTEGER,
        Q2 INTEGER,
        Q3 INTEGER,
        Q4 INTEGER,
        Q5 INTEGER,
        Q6 INTEGER,
        Q7 INTEGER,
        Q8 INTEGER,
        Q9 INTEGER,
        Q10 INTEGER,
        Q11 INTEGER,
        Q12 INTEGER,
        Q13 INTEGER,
        Grade INTEGER
    );
    '''
    cursor.executescript(create_table_query)

    conn.commit()
    conn.close()

def add_data_to_database():
    # Call your cleaning functions to get the cleaned data
    dfMock_Test = load_and_clean_data_Mock_Test()
    dfFormative_Test_1 = load_and_clean_data_Formative_Test_1()
    dfFormative_Test_2 = load_and_clean_data_Formative_Test_2()
    dfFormative_Test_3 = load_and_clean_data_Formative_Test_3()
    dfFormative_Test_4 = load_and_clean_data_Formative_Test_4()
    dfStudentRate = load_and_clean_data_StudentRate()
    dfSumTest = load_and_clean_data_SumTest()

    # Connect to the SQLite database
    db_path = os.path.join('data', 'ResultsDatabase.db')
    conn = sqlite3.connect(db_path)
    
    # Use pandas to_sql method to insert data into respective tables
    dfMock_Test.to_sql('Mock_Test', conn, if_exists='replace', index=False)
    dfFormative_Test_1.to_sql('Formative_Test_1', conn, if_exists='replace', index=False)
    dfFormative_Test_2.to_sql('Formative_Test_2', conn, if_exists='replace', index=False)
    dfFormative_Test_3.to_sql('Formative_Test_3', conn, if_exists='replace', index=False)
    dfFormative_Test_4.to_sql('Formative_Test_4', conn, if_exists='replace', index=False)
    dfStudentRate.to_sql('StudentRate', conn, if_exists='replace', index=False)
    dfSumTest.to_sql('SumTest', conn, if_exists='replace', index=False)

    conn.close()

create_database()
add_data_to_database()