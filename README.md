# python_project_8


PR. 8 - Analyzer
NumPy Analyzer | PYTHON - DATA SCIENCE
Menu-driven NumPy Analyzer je NumPy functionalities ane OOP principles ne integrate kare che.

Objective
User ne common data operations, statistical analyses ane mathematical computations
NumPy arrays par karva deva.

Features
Class and Object Structure
DataAnalytics class badhi functionalities ne encapsulate kare che
Array Management
Creation, Indexing, Slicing: 1D, 2D, 3D arrays
Combining and Splitting: concatenate, vstack, hstack, split
Mathematical Operations
Element-wise Addition, Subtraction, Multiplication, Division
Dot Product ane Matrix Multiplication for 2D arrays
Search, Sort, and Filter
Search specific value
Sort ascending / descending (row-wise)
Filter based on user-defined conditions - >, <, ==, Even, Odd
Aggregating Functions
Sum, Mean, Median, Standard Deviation, Variance
Statistical Functions
Minimum and Maximum values
Percentiles - 25th, 50th, 75th
Correlation coefficients between arrays
OOP
Constructor for initializing arrays
Encapsulation ane private methods __validate_array, __get_elements, __parse_range
Private attribute __array
Class-level method @classmethod - get_project_name()
Static method @staticmethod - show_welcome(), is_valid_shape()
User Interface (UI)
Menu-driven interface
Exit from main menu
How to Run
pip install numpy
python numpy_analyzer.py
Example Console Interaction
Welcome Start:
Welcome to the NumPy Analyzer!
=======================================================
Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
Enter your choice: 1
Array Creation:
Select the type of array to create:
1. 1D Array
2. 2D Array
3. 3D Array
Enter your choice: 2
Enter the number of rows: 2
Enter the number of columns: 3
Enter 6 elements for the array separated by space: 10 20 30 40 50 60
Array created successfully:
[[10 20 30]
 [40 50 60]]

Choose an operation:
1. Indexing
2. Slicing
3. Go Back
Enter your choice: 2
Enter the row range (start:end): 0:2
Enter the column range (start:end): 1:3
Sliced Array:
[[20 30]
 [50 60]]
Mathematical Operations:
Choose a mathematical operation:
1. Addition
Enter your choice: 1
Enter 6 elements for the array separated by space: 5 5 5 5 5 5
Original Array:
[[10 20 30]
 [40 50 60]]
Second Array:
[[5 5 5]
 [5 5 5]]
Result of Addition:
[[15 25 35]
 [45 55 65]]
Combine:
Combined Array (Vertical Stack):
[[10 20 30]
 [40 50 60]
 [ 1  2  3]
 [ 4  5  6]]
Aggregates:
Median of Array: 35.0
Assumptions
User numbers space thi alag kari ne nakhse. Ex: 10 20 30
Second array mate same size no array joiye che.
Division mate second array ma 0 na hovo joiye.
Matrix Multiplication mate banne 2D arrays ane compatible shape joiye.
Correlation mate banne array same size na hova joiye.
Requirements
Python 3.8+
numpy - pip install numpy
