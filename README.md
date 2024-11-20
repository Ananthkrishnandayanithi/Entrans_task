Data Analysis and Visualization Project
Overview

This project involves analyzing a dataset using Pandas, Seaborn, and Matplotlib. The dataset contains various types of information, including numerical, categorical, and temporal data. The analysis is structured in a modular way, with classes and functions to handle different tasks, ensuring readability and reusability of the code.

Features

Preprocessing:

Class for Data Preprocessing:
Check Missing/Duplicate Values: Identifies missing and duplicate entries in the dataset.
Column Data Types: Analyzes the type of data in each column.
Numerical Summary

Class for Numerical Summary:

Provides key metrics like mean, median, and mode for numerical columns.
Exploratory Analysis Tasks
Each task is implemented as a separate function for clarity and modularity:

Task 1: Unique Values

Created a function to get unique values in the following columns:
Product_Category
Sub_Category
Product

Task 2: Histogram of Age and Frequency

Plotted a histogram to analyze the frequency distribution of ages.

Task 3: Filtering Data by Year

Developed a function that:
Takes a year as input.
Filters the dataset for that year.
Plots a histogram for the filtered data.

Task 4: Gender Distribution

Created a pie chart to visualize the distribution of genders.

Task 5: Age Group and Revenue

Used a bar chart to show the relationship between Age_Group and Revenue.
Identified the age group that generates the most revenue.

Task 6: Profitable Product Categories

Grouped data by Product_Category and summed up profits to:
Identify the most and least profitable categories.
Created a horizontal bar chart showing profits by category.

Task 7: Revenue and Profit Trends

Implemented a function to:
Take user input for start and end months/years.
Create a line plot to show revenue and profit trends over the specified period.

Task 8: Profit Margin Analysis

Calculated the average profit margin per product.
Visualized the data using a scatter plot.

Task 9: Sub-Category Performance

Examined which Sub_Category within a Product_Category performs best in terms of:
Profit
Revenue
Grouped data by Product_Category and Sub_Category to calculate totals.
Created a stacked bar chart to show revenue/profit by sub-category within categories.

Technologies Used
Python
Pandas: For data manipulation and preprocessing.
Seaborn: For advanced visualizations.
Matplotlib: For creating detailed plots.
