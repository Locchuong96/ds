'''
python3 DV0101EN-Final_Assign_Part_2_Questions.py
'''

import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# Load the data using pandas
data = pd.read_csv('data/historical_automobile_sales.csv')

#---------------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------

# # Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    
    # Title
    html.H1('Automobile Sales Statistics Dashboard', 
    style={'textAlign': 'center', 'color': '#503D36',
    'font-size': 30,'width': '80%'}),
    
    # Dropout 1
    html.H1([
        html.H2('Select Report:', style={'margin-right': '2em','font-size': 20}),
        dcc.Dropdown(id= 'dropdown-statistics', 
                options= dropdown_options,
                placeholder= 'Select a report type',
                style= {'textAlign': 'left', 'color': '#503D36', 'font-size': 20, 'width': '80%','padding':3})
        ]),
    
    # Dropout 2
    html.H1([
        html.H2('Select Year:', style= {'margin-right': '2em','font-size': 20}),
        dcc.Dropdown(id= 'select-year',
                     options= [{'label': i, 'value': i} for i in year_list]),],
                    style= {'textAlign': 'left', 'color': '#503D36', 'font-size': 20, 'width': '80%','padding':3}
        ),
    
    # Output
    html.Div([
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),])
    ])

# Create the layout of the app
@app.callback(
    Output(component_id='select-year', component_property='value'),
    Input(component_id='dropdown-statistics', component_property='value'))

def update_input_container(input_statistics):
    if input_statistics =='Yearly Statistics': 
        print('Yearly Statistics Selected')
        return False
    else:
        print('Recession Period Statistics')
        return True
    
#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='select-year', component_property='value'),
     Input(component_id='dropdown-statistics', component_property='value')])

def update_output_container(input_year,select_statstics):
    
    if select_statstics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
        #Plot 1 Automobile sales fluctuate over Recession Period (year wise) using line chart
        # grouping data for plotting
        yearly_rec=recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        # Plotting the line graph
        R_chart1 = dcc.Graph(figure=px.line(yearly_rec, 
                                            x='Year',
                                            y='Automobile_Sales',
                                            title="Automobile sales fluctuate over Recession Period (year wise)"))
        
        #Plot 2 Calculate the average number of vehicles sold by vehicle type and represent as a Bar chart
        typely_rec=recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        # Plotting the line graph
        R_chart2 = dcc.Graph(figure=px.bar(typely_rec, 
                                            x='Vehicle_Type',
                                            y='Automobile_Sales',
                                            title="The average number of vehicles sold by vehicle type"))
        
        # Plot 3 : Pie chart for total expenditure share by vehicle type during recessions
        # grouping data for plotting
        exp_rec= recession_data.groupby("Vehicle_Type")["Advertising_Expenditure"].sum().reset_index()
        R_chart3 = dcc.Graph(
                figure=px.pie(exp_rec,
                names="Vehicle_Type",
                values="Advertising_Expenditure",
                title="Total Expenditure Share by Vehicle Type During Recession")
        )
        
        # Plot 4 Develop a Bar chart for the effect of unemployment rate on vehicle type and sales
        unemp_rate= recession_data.groupby("Vehicle_Type")["unemployment_rate"].mean().reset_index()
        R_chart4 = dcc.Graph(
                figure=px.bar(unemp_rate,
                x="Vehicle_Type",
                y="unemployment_rate",
                title="Effect of Unemployment Rate on Vehicle Type and Sales")
        )
        
        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1),html.Div(children=R_chart2)],style={"display": "flex"}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3),html.Div(children=R_chart4)],style={"display": "flex"})
            ]
        
    elif (input_year and select_statstics=='Yearly Statistics') :
        
        yearly_data = data[data['Year'] == input_year]
        
        #plot 1 Yearly Automobile sales using line chart for the whole period.
        yas= data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(yas, 
                                            x='Year',
                                            y='Automobile_Sales',
                                            title="Yearly Automobile sales {}".format(input_year)))
        
        # Plot 2 :Total Monthly Automobile sales using line chart.
        total_monthly=yearly_data.groupby("Month")["Automobile_Sales"].sum().reset_index()
        Y_chart2 = dcc.Graph( figure=px.line(total_monthly, 
                                            x='Month',
                                            y='Automobile_Sales',
                                            title='Monthly Automobile sales {}'.format(input_year)))
        
        # Plot bar chart for average number of vehicles sold during the given year
        avr_vdata=yearly_data.groupby("Vehicle_Type")["Automobile_Sales"].mean().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(avr_vdata,
                                        x="Vehicle_Type",
                                        y="Automobile_Sales",
                                        title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))
        
        # Total Advertisement Expenditure for each vehicle using pie chart
        exp_data=yearly_data.groupby("Advertising_Expenditure")["Vehicle_Type"].sum().reset_index()
        Y_chart4 = dcc.Graph(figure=px.pie(exp_data,
                                            names="Vehicle_Type",
                                            values="Advertising_Expenditure",
                                            ))
        
        return [
            html.Div(className='chart-item', children=[html.Div(children=Y_chart1),html.Div(children=Y_chart2)],style={"display": "flex"}),
            html.Div(className='chart-item', children=[html.Div(children=Y_chart3),html.Div(children=Y_chart4)],style={"display": "flex"})
            ]

# # Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=False)

