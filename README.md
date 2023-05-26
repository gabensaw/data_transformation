# Data Transformation
This repository contains a Python script for reading a file, performing data transformation, and saving the transformed data to a new file. The script and the resulting clean file are uploaded to GitHub.

## Task Description
The task involves the following steps:

- Read the input file in Python.
- Perform transformations on the data.
- Remove rows with missing values.
- Remove rows where the student was absent for all assessments.
- Remove the columns Zscore, gender, and syllabus.
- Concatenate the three date columns (birth_day, birth_month, birth_year) into one column (birthdate).
- Save the transformed data to a new file.
- Upload the code and the clean file to GitHub.

## Implementation
The implementation of the data transformation can be found in the data_transformation.py file. The script follows the steps described below:

1. Reading the File: The script reads the input file using appropriate Python libraries.
2. Data Transformation: The transformations, as specified in the task description, are applied to the data using pandas.
3. Removing Rows: Rows with missing values and rows where the student was absent for all assessments are removed.
4. Removing Columns: The columns Zscore, gender, and syllabus are dropped from the dataframe.
5. Concatenating Date Columns: The three date columns (birth_day, birth_month, birth_year) are concatenated into a single column (birthdate).
6. Saving the Clean File: The resulting clean dataframe is saved to a new CSV file.
7. Comments: Detailed comments are provided in the data_transformation.py file, explaining the steps followed in reading the file, performing the transformations, and writing the clean data to the new file.

## Usage
To use the data transformation script:

1. Clone this repository to your local machine.
2. Open the data_transformation.py file and review the comments for understanding the implementation steps.
3. Run the script using a Python interpreter.
4. The clean data will be saved as a new CSV file.

## Contribution
Contributions to this project are welcome. If you have any suggestions for improvements or would like to add new features, please submit a pull request.

## Author
Gabriel Sawicki
