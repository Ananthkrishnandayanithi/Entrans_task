# Install necessary packages
# pip install pandas matplotlib seaborn openpyxl

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import pickle

# Load the dataset
df = pd.read_excel('D:\\Entrans_task\\sales_data.xlsx')
import os
# Save the processed DataFrame as a pickle file
def save_dataframe_as_pickle(dataframe, filename="processed_data.pkl"):
    
    try:
        # Get the script's current directory
        current_dir = os.getcwd()
        output_path = os.path.join(current_dir, filename)

        # Save the DataFrame as a pickle file
        with open(output_path, 'wb') as file:
            pickle.dump(dataframe, file)

        print(f"DataFrame saved as pickle file: {output_path}")
    except Exception as e:
        print(f"Error saving pickle file: {e}")

# Call the save function
save_dataframe_as_pickle(df)

class Preprocessing:
    def precheck(self):
        print("Missing Values:")
        print(df.isnull().sum())
        print("\nDuplicate Columns:")
        print(df.columns.duplicated())

    def dtype(self):
        print("\nData Types:")
        for col in df.columns:
            print(f"{col}: {df[col].dtype}")

# Initialize and check preprocessing
preprocess = Preprocessing()
preprocess.precheck()
preprocess.dtype()

# Summary statistics for numerical columns
class NumericalSummary:
    def NumSummary(self):
        numerical_cols = ['Order_Quantity', 'Unit_Price', 'Profit', 
                          'Revenue', 'Cost', 'Unit_Cost', 'Customer_Age']
        for col in numerical_cols:
            print(f"\nColumn: {col}")
            print(f"Mean: {df[col].mean()}")
            print(f"Median: {df[col].median()}")
            print(f"Mode: {df[col].mode().tolist()}")
            print("-" * 30)

num_summary = NumericalSummary()
num_summary.NumSummary()

# Unique values in selected columns
def unique_values():
    cols = ['Product_Category', 'Sub_Category', 'Product']
    for col in cols:
        print(f"\nUnique values in {col}:")
        print(df[col].unique())
        print("-" * 80)

unique_values()

# Plotting Customer Age Distribution
def hist_customer_age():
    df.hist(column='Customer_Age', bins=50, color='#86bf91')
    plt.title("Age Distribution")
    plt.xlabel("Customer Age")
    plt.ylabel("Frequency")
    plt.show()

hist_customer_age()

# Pie chart for customer gender distribution
def pie_chart():
    gender_counts = df['Customer_Gender'].value_counts()
    gender_counts.plot.pie(
        autopct='%1.1f%%',
        figsize=(5, 5),
        startangle=90,
        colors=['skyblue', 'pink']
    )
    plt.title("Customer Gender Distribution")
    plt.ylabel("")
    plt.show()

pie_chart()

# Bar graph for Revenue by Age Group
def revenue_by_age_group():
    plt.figure(figsize=(8, 5))
    plt.bar(df['Age_Group'], df['Revenue'])
    plt.xlabel("Age Group")
    plt.ylabel("Revenue")
    plt.title("Revenue by Age Group")
    plt.show()

revenue_by_age_group()

# Profit by Product Category
def profit_by_category():
    total_profit = df.groupby('Product_Category')['Profit'].sum()
    total_profit.plot.barh(color='green', title='Profit by Category')
    plt.xlabel('Total Profit')
    plt.ylabel('Product Category')
    plt.show()

profit_by_category()

# Line graph for revenue and profit trends
def line_graph(start_date, end_date):
    try:
        date_format = "%Y-%m-%d"
        start_date = datetime.strptime(start_date, date_format)
        end_date = datetime.strptime(end_date, date_format)

        df['Date'] = pd.to_datetime(df['Date'])
        filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        filtered_df['YearMonth'] = filtered_df['Date'].dt.to_period('M')

        monthly_data = filtered_df.groupby('YearMonth').agg({'Revenue': 'sum', 'Profit': 'sum'}).reset_index()

        plt.figure(figsize=(12, 6))
        plt.plot(monthly_data['YearMonth'].astype(str), monthly_data['Revenue'], marker='o', label='Revenue', color='green')
        plt.plot(monthly_data['YearMonth'].astype(str), monthly_data['Profit'], marker='x', label='Profit', color='blue')
        plt.title("Revenue and Profit Trends")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

line_graph('2023-01-01', '2023-12-31')

# Scatter plot for profit margin
def scatter_plot_profit_margin():
    total_profit = df['Profit'].sum()
    profit_margin = (df.groupby('Product')['Profit'].mean() / total_profit) * 100
    profit_margin_df = profit_margin.reset_index()
    profit_margin_df.rename(columns={'Profit': 'Profit_Margin'}, inplace=True)
    profit_margin_df['Product_Num'] = range(len(profit_margin_df))

    plt.figure(figsize=(30, 15))
    plt.scatter(profit_margin_df['Product_Num'], profit_margin_df['Profit_Margin'], color='blue', alpha=0.7)
    plt.xticks(profit_margin_df['Product_Num'], profit_margin_df['Product'], rotation=45)
    plt.xlabel('Product')
    plt.ylabel('Profit Margin (%)')
    plt.title('Profit Margin by Product')
    plt.tight_layout()
    plt.show()

scatter_plot_profit_margin()

# Revenue distribution by age group for each year
def boxplot_revenue_age_group():
    years = df['Year'].unique()
    fig, axes = plt.subplots(1, len(years), figsize=(20, 6), sharey=True)
    fig.suptitle('Revenue Distribution by Age Group for Each Year', fontsize=16)

    for ax, year in zip(axes, years):
        yearly_df = df[df['Year'] == year]
        sns.boxplot(x='Age_Group', y='Revenue', data=yearly_df, ax=ax)
        ax.set_title(f'Year {year}')
        ax.set_xlabel('Age Group')
        ax.set_ylabel('Revenue')
        ax.grid(True)

    plt.tight_layout()
    plt.show()

boxplot_revenue_age_group()

# 3D Bar chart for state-wise profit
class DataVisualizer:
    def __init__(self, dataframe):
        self.df = dataframe

    def state_high_profit(self):
        state_profit = self.df.groupby('State')['Profit'].sum()
        states = state_profit.index
        profits = state_profit.values

        fig = plt.figure(figsize=(30, 30))
        ax = fig.add_subplot(111, projection='3d')
        xpos = range(len(states))
        ypos = [0] * len(states)
        zpos = [0] * len(states)
        dx = dy = 0.5
        dz = profits

        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='maroon', alpha=0.8)
        ax.set_xticks(xpos)
        ax.set_xticklabels(states, rotation=45, ha='right')
        ax.set_xlabel("States")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Profit")
        ax.set_title("State-wise Profit (3D Bar Chart)")
        plt.show()

    def pie_chart_profit(self):
        state_profit = self.df.groupby('State')['Profit'].sum()
        state_profit.plot.pie(
            autopct='%1.1f%%',
            shadow=True,
            figsize=(8, 8),
            startangle=90
        )
        plt.title("Profit Distribution by State")
        plt.ylabel("")
        plt.show()

visualizer = DataVisualizer(df)
visualizer.state_high_profit()
visualizer.pie_chart_profit()

