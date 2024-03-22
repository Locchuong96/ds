'''
python3 DV0101EN-Final_Assign_Part_2_Questions.py
'''

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('data/historical_automobile_sales.csv')

# # Initialize the Dash app
app = dash.Dash(__name__)

dropdown_options = [
    {'label': '...........', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': '.........'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]


# # Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=False)

