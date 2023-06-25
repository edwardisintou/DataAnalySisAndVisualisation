"""
Project2 2023 CITS 2401 Computer Analysis and Visualisation
Author: Edward Le
Student ID: 23020568
This projects continues from project1
with focus on data analysis and visualisation skills
Project contains 3 parts:
Part 1: Data Analysis using NumPy
Part 2: Data Visualisation using matplotlib
Part 3: Write a summary report
The code below is used for part 1 and 2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Task1():
    """
    this class includes all function needed for task1
    it takes 2 data file and get data from each file
    also, we can analysis more than 2 dataset files
    using the same method
    """
    def __init__(self, filename1, filename2, file_number=1):
        """init function"""
        try: #check if filename is incorrect
            self.data1 = pd.read_csv(filename1)
            self.data2 = pd.read_csv(filename2)

            self.file_number = file_number
            self.data = self.check_file_number()
        except (FileNotFoundError, IOError):
            print(f"file {filename1} or {filename2} not found, please check again")

    def check_file_number(self):
        """
        function to check which file of dataset is used
        the first file is used by default (file_number=1)
        if we want to use the second file then
        file_number parameter is 2 when creating Task1 instance
        """
        if(self.file_number == 2):
            return self.data2
        return self.data1

    def overall(self):
        """this function returns the overall look of data"""
        return self.data
    
    def get_descriptive_statistics(self):
        """
        this function returns the describe of the data
        data is only returned if they are numeric
        statistics like count, mean, std,... are calculated
        """
        return self.data.describe()

    def get_unique_values_count(self, column_name):
        """
        return unique value of each value in a column
        and also its count
        """
        return np.unique(self.data[column_name], return_counts=True)
    
    def select_specific_rows_and_columns(self, rows, columns):
        """return specific value of a row and column"""
        return self.data.iloc[rows-1, columns]
    
    def difference(self, column_name):
        """return value in first column subtract value in second one"""
        return self.data1[column_name] - self.data2[column_name]
    
    def stack_data(self):
        """stack value according to same column between 2 files"""
        return np.vstack(self.data1, self.data2)
    
    def condition(self, column_name, compare_value):
        """
        return new 2D array, each small array contain
        value that match condition 
        """
        array = np.array(self.data)
        return array[np.where(self.data[column_name] == compare_value)]
        
        
class Task2():
    """
    this class provides all method needed for task 2
    similar to class task1, the class can take more than
    1 datafile as parameters but I take 2 of that here
    """
    def __init__(self, filename1, filename2, file_number=1):
        """init function"""
        try: #check if filename is incorrect
            self.data1 = pd.read_csv(filename1)
            self.data2 = pd.read_csv(filename2)

            self.file_number = file_number
            self.data = self.check_file_number()
        except (FileNotFoundError, IOError):
            print(f"file {filename1} or {filename2} not found, please check again")

    def check_file_number(self):
        """check which file is used"""
        if(self.file_number == 2):
            return self.data2
        return self.data1

    def plot_line_chart(self):
        """plot the line chart using timestamp"""
        plt.plot(self.data['Timestamp'])
        plt.title('Timestamp Line Chart')
        plt.xlabel('Index')
        plt.ylabel('Timestamp')
        plt.show()

    def plot_line_plot(self):
        """plot the line plot of timestamps categorized by class"""
        normal_timestamps = self.data[self.data['Class'] == 'Normal']['Timestamp']
        attack_timestamps = self.data[self.data['Class'] == 'Attack']['Timestamp']

        plt.plot(normal_timestamps, label='Normal')
        plt.plot(attack_timestamps, label='Attack')

        plt.xlabel('Timestamp')
        plt.ylabel('Class')
        plt.title('Timestamp by Class')
        plt.legend()
        plt.show()

    def plot_bar_chart(self):
        """plot bar chart that displays the count of events for each class"""
        class_counts = self.data['Class'].value_counts()

        plt.bar(class_counts.index, class_counts.values)
        plt.title('Class Bar Chart')
        plt.xlabel('Class')
        plt.ylabel('Count')
        plt.show()

    def plot_grouped_bar_chart(self):
        """
        plot grouped bar chat with distribution of DLC values
        within each combination of Class and SubClass labels
        """
        grouped_data = self.data.groupby(['Class', 'SubClass'])['DLC'].mean().unstack()

        plt.figure(figsize=(10, 6))
        grouped_data.plot(kind='bar')
        plt.xlabel('Class')
        plt.ylabel('Average DLC')
        plt.title('Average DLC Distribution by Class and SubClass')
        plt.legend(title='SubClass')
        plt.show()

    def plot_pie_chart(self):
        """plot a pie chart representing the distribution of subclasses"""
        sub_class = self.data['SubClass'].value_counts()

        plt.pie(sub_class, labels=sub_class.index, autopct='%1.1f%%')
        plt.title('SubClass Distribution')
        plt.axis('equal')
        plt.show()

    def plot_histogram(self):
        """plot histogram of the DLC values"""
        plt.hist(self.data['DLC'], bins=10)
        plt.title('DLC Histogram')
        plt.xlabel('DLC')
        plt.ylabel('Count')
        plt.show()


"""
below are some example test cases that were used
for analysing different problems
""" 
# task1 = Task1("proj1_data1.csv", "proj1_data2.csv")
# print(task1.overall())
# print(task1.get_descriptive_statistics())
# print(task1.get_unique_values_count("Arbitration_ID"))
# print(task1.select_specific_rows_and_columns(1, 3))
# print(task1.difference("Timestamp"))
# print(task1.condition("Class", "Attack"))
# new_data = task1.stack_data()
# print(new_data)
# print(len(new_data))

# task2 = Task2("proj1_data1.csv", "proj1_data2.csv")
# task2.plot_line_chart()
# task2.plot_line_plot()
# task2.plot_bar_chart()
# task2.plot_grouped_bar_chart()
# task2.plot_pie_chart()
# task2.plot_histogram()