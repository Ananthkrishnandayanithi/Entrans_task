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
![image](https://github.com/user-attachments/assets/8a0ff4f3-324f-41a5-87a4-e61488e11b95)


Task 3: Filtering Data by Year

Developed a function that:
Takes a year as input.
Filters the dataset for that year.
Plots a histogram for the filtered data.

Task 4: Gender Distribution

Created a pie chart to visualize the distribution of genders.
![image](https://github.com/user-attachments/assets/d6578641-3cc1-4d36-b8b5-eac34f7c4a16)


Task 5: Age Group and Revenue

Used a bar chart to show the relationship between Age_Group and Revenue.
Identified the age group that generates the most revenue.
![image](https://github.com/user-attachments/assets/fb31f0e2-7a7d-47c2-9d26-43a71b8cd834)


Task 6: Profitable Product Categories

Grouped data by Product_Category and summed up profits to:
Identify the most and least profitable categories.
Created a horizontal bar chart showing profits by category.
![image](https://github.com/user-attachments/assets/5370228b-90d4-4f85-8fd7-96eab2eea984)


Task 7: Revenue and Profit Trends

Implemented a function to:
Take user input for start and end months/years.
Create a line plot to show revenue and profit trends over the specified period.
![image](https://github.com/user-attachments/assets/03b67014-e450-4e6a-b841-2e2011a48243)


Task 8: Profit Margin Analysis

Calculated the average profit margin per product.
Visualized the data using a scatter plot.
![image](https://github.com/user-attachments/assets/56a3eeba-9559-43ca-bd32-badd1af05430)


Task 9: Sub-Category Performance

Examined which Sub_Category within a Product_Category performs best in terms of:
Profit
Revenue
Grouped data by Product_Category and Sub_Category to calculate totals.
Created a stacked bar chart to show revenue/profit by sub-category within categories.
![image](https://github.com/user-attachments/assets/e1b04180-d1aa-4a13-a9b4-93e5ca3410eb)
Task 10: Revenue Distribution by Age Group for Each Year
The `subplot` function creates side-by-side box plots to visualize the distribution of revenue by age group for each year. This helps identify trends, outliers, and variability in revenue generation within different age groups over multiple years.
![image](https://github.com/user-attachments/assets/5d2f92de-54be-4e6c-9905-cf1f2eae3998)

Task 11: Advanced Data Visualizations

1. 3D Bar Chart for State-Wise Profit
- Displays state-wise total profits using a 3D bar chart.
- Customizes axes for better readability and visual appeal.
![image](https://github.com/user-attachments/assets/400de4d8-427b-46eb-a103-a6aa3e0efd90)

2. Pie Chart for Profit Distribution
- Visualizes profit distribution across states using a pie chart with an explode effect for emphasis.
![image](https://github.com/user-attachments/assets/56d437e0-4a1a-4fa5-8b6d-80d874810fc3)
3. Scatter Plot for Gender Distribution
- Illustrates the distribution of customer genders across different product categories in a scatter plot.
- Helps identify patterns in gender preferences for products.
![image](https://github.com/user-attachments/assets/1220f516-6b94-4357-a9e6-50da36dd5e58)

Technologies Used
Python
Pandas: For data manipulation and preprocessing.
Seaborn: For advanced visualizations.
Matplotlib: For creating detailed plots.
