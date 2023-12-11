import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to read and clean the data
def read_and_clean_data(filepath):
    """
    Reads and cleans the data from the given CSV file.

    Parameters:
    filepath (str): The path to the CSV file.

    Returns:
    DataFrame: The cleaned pandas DataFrame.
    """
    data = pd.read_csv(filepath)
    cleaned_data = data.drop([0, 1, 2])
    cleaned_data.columns = cleaned_data.iloc[0]
    cleaned_data = cleaned_data.drop(3)
    cleaned_data.reset_index(drop=True, inplace=True)
    return cleaned_data

# Function to create a clear line plot
def create_line_plot(data, title, xlabel, ylabel):
    """
    Creates a clear line plot with straight lines and distinct colors for each line.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the data to plot.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    """
    plt.figure(figsize=(12, 6))
    colors = plt.cm.viridis(np.linspace(0, 1, len(data.columns)))
    for i, column in enumerate(data.columns):
        plt.plot(data.index, data[column], label=column, color=colors[i], linewidth=2)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to create a colored bar chart
def create_bar_chart(data, title, xlabel, ylabel):
    """
    Creates a colored bar chart for the given data.

    Parameters:
    data (Series): The pandas Series containing the data to plot.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    """
    plt.figure(figsize=(12, 6))
    data.plot(kind='bar', color=plt.cm.Paired(np.arange(len(data))))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

# Function to create a visible pie chart
def create_pie_chart(data, title):
    """
    Creates a pie chart with clear visibility of values for each segment.

    Parameters:
    data (Series): The pandas Series containing the data to plot.
    title (str): The title of the plot.
    """
    plt.figure(figsize=(8, 8))
    data.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(np.arange(len(data))), pctdistance=0.85)
    plt.title(title)
    plt.ylabel('')  # Hides the y-label
    plt.show()

# Reading and cleaning the data
file_path = 'Number-and-types-of-applications-by-all-account-customers-2023-11.csv'  # Replace with your actual file path
cleaned_data = read_and_clean_data(file_path)

# Aggregating data for line plot
time_series_data = cleaned_data.drop(['Account Customer', 'Total'], axis=1).astype(int).cumsum()
time_series_data.index = range(1, len(time_series_data) + 1)

# Aggregating data for bar and pie charts
total_applications = cleaned_data.drop(['Account Customer', 'Total'], axis=1).astype(int).sum()

# Creating the visualizations
create_line_plot(time_series_data, "Trend of Application Types Over Time", "Time Point", "Number of Applications")
create_bar_chart(total_applications, "Total Number of Applications for Each Type", "Application Type", "Total Applications")
create_pie_chart(total_applications, "Proportion of Each Application Type")
