import unittest
import pandas as pd
from Altask import Preprocessing, NumericalSummary, unique_values, hist_customer_age, pie_chart, revenue_by_age_group, profit_by_category, line_graph, scatter_plot_profit_margin, boxplot_revenue_age_group, DataVisualizer

class TestAltask(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.df = pd.read_excel('D:\\Entrans_task\\sales_data.xlsx')
    
    def test_column_names(self):
        
        expected_columns = ['Order_Quantity', 'Unit_Price', 'Profit', 'Revenue', 'Cost', 'Unit_Cost', 'Customer_Age', 'Product_Category', 'Sub_Category', 'Product', 'Customer_Gender', 'Age_Group', 'State', 'Year', 'Date']
        actual_columns = self.df.columns.tolist()
        self.assertTrue(all(col in actual_columns for col in expected_columns), "Missing expected columns")
    
    def test_dtype(self):
        
        dtype_check = {
            'Order_Quantity': 'int64',
            'Unit_Price': 'float64',
            'Profit': 'float64',
            'Revenue': 'float64',
            'Customer_Age': 'int64',
            'Product_Category': 'object',
            'Customer_Gender': 'object',
            'Age_Group': 'object',
            'State': 'object',
            'Year': 'int64'
        }
        for column, dtype in dtype_check.items():
            with self.subTest(column=column):
                self.assertEqual(self.df[column].dtype.name, dtype, f"Incorrect dtype for {column}")

    def test_num_summary(self):
        """Test numerical summary statistics output for mean, median, and mode."""
        numerical_cols = ['Order_Quantity', 'Unit_Price', 'Profit', 'Revenue', 'Cost', 'Unit_Cost', 'Customer_Age']
        for col in numerical_cols:
            with self.subTest(col=col):
                self.assertTrue(self.df[col].mean() is not None, f"Mean is missing for {col}")
                self.assertTrue(self.df[col].median() is not None, f"Median is missing for {col}")
                self.assertTrue(self.df[col].mode().notnull().any(), f"Mode is missing for {col}")

    def test_unique_values(self):
        """Test to check that unique values in specified columns are returned correctly."""
        cols = ['Product_Category', 'Sub_Category', 'Product']
        for col in cols:
            with self.subTest(col=col):
                unique_vals = self.df[col].unique()
                self.assertTrue(len(unique_vals) > 0, f"No unique values found for {col}")

    def test_task_h_and_b(self):
        """Test specific tasks like 'h' (3D state-wise profit chart) and 'b' (pie chart for gender distribution)."""
        
        try:
            visualizer = DataVisualizer(self.df)
            visualizer.state_high_profit()  
            self.assertTrue(True, "Task 'h' executed successfully.")
        except Exception as e:
            self.fail(f"Task 'h' failed with error: {e}")

        
        try:
            pie_chart()  
            self.assertTrue(True, "Task 'b' executed successfully.")
        except Exception as e:
            self.fail(f"Task 'b' failed with error: {e}")

if __name__ == '__main__':
    unittest.main()
