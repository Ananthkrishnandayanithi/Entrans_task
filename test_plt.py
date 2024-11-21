import sys
import importlib.util

# Add directory containing Altask.py to sys.path
sys.path.append(r'D:\Entrans_task')

# Check if Altask module is accessible using importlib
module_name = 'Altask'
spec = importlib.util.find_spec(module_name)

if spec is not None:
    print(f"{module_name} module found.")
else:
    print(f"{module_name} module not found.")

import unittest
from unittest.mock import patch
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Test Class
class TestAltaskFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load the test data
        cls.df = pd.read_excel('D:/Entrans_task/sales_data.xlsx')

    def test_precheck(self):
        with patch('builtins.print') as mocked_print:
            Altask.preprocessing().precheck()
            mocked_print.assert_any_call("Missing Values:")

    def test_dtype(self):
        with patch('builtins.print') as mocked_print:
            Altask.preprocessing().dtype()
            mocked_print.assert_any_call("\nData Types:")

    def test_num_summary(self):
        with patch('builtins.print') as mocked_print:
            Altask.NumericalSummary().NumSummary()
            mocked_print.assert_any_call("Column: Order_Quantity")

    def test_unique_values(self):
        with patch('builtins.print') as mocked_print:
            Altask.task2()
            mocked_print.assert_any_call("Unique values in Product_Category:")

    def test_hist_custage(self):
        with patch.object(plt, 'show') as mocked_show:
            Altask.hist_custage()
            mocked_show.assert_called_once()

    def test_pie(self):
        with patch.object(plt, 'show') as mocked_show:
            Altask.pie()
            mocked_show.assert_called_once()

    def test_bargraph(self):
        with patch.object(plt, 'show') as mocked_show:
            Altask.bargraph()
            mocked_show.assert_called_once()

    def test_product_category(self):
        with patch.object(plt, 'show') as mocked_show:
            with patch('builtins.print') as mocked_print:
                Altask.product_category()
                mocked_print.assert_any_call("Summation of Max Profits:")
                mocked_show.assert_called_once()

    def test_linegraph(self):
        start_date = "2023-01-01"
        end_date = "2023-12-31"
        with patch.object(plt, 'show') as mocked_show:
            Altask.linegraph(start_date, end_date)
            mocked_show.assert_called_once()

    def test_profit_margin_by_product(self):
        with patch.object(plt, 'show') as mocked_show:
            Altask.profit_margin_by_product()
            mocked_show.assert_called_once()

    def test_subplot(self):
        with patch.object(plt, 'show') as mocked_show:
            Altask.subplot()
            mocked_show.assert_called()

    def test_analyze_and_plot_profit(self):
        with patch.object(plt, 'show') as mocked_show:
            Altask.analyze_and_plot(value_column='Profit')
            mocked_show.assert_called_once()

    def test_analyze_and_plot_revenue(self):
        with patch.object(plt, 'show') as mocked_show:
            Altask.analyze_and_plot(value_column='Revenue')
            mocked_show.assert_called_once()

    def test_state_high_profit(self):
        with patch.object(plt, 'show') as mocked_show:
            Altask.state_high_profit()
            mocked_show.assert_called_once()

    def test_scatter_gender(self):
        with patch.object(plt, 'show') as mocked_show:
            Altask.scatter_gender()
            mocked_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
