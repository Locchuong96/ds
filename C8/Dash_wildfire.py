import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update
import datetime as dt

#Create app

app = dash.Dash(__name__)

# Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Read the wildfire data into pandas dataframe
df =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv')

#Extract year and month from the date column

df['Month'] = pd.to_datetime(df['Date']).dt.month_name() #used for the names of the months
df['Year'] = pd.to_datetime(df['Date']).dt.year

#Layout Section of Dash

#Task 2.1 Add the Title to the Dashboard
app.layout = html.Div(children=[html.H1(..................),

# TASK 2.2: Add the radio items and a dropdown right below the first inner division
#outer division starts
     html.Div([
                   # First inner divsion for  adding dropdown helper text for Selected Drive wheels
                    html.Div([
                            html.H2(.........),

                    #Radio items to select the region
                    #dcc.RadioItems(['NSW',.....], value ='...', id='...',inline=True)]),
                    dcc.RadioItems([{"label":"New South Wales","value": "NSW"},
                                    {..........},
                                    {..........},
                                    {..........},
                                    {..........},
                                    {..........},
                                    {"label":"...","value": ..}], value = "...", id='.....,inline=True)]),
                    #Dropdown to select year
                    html.Div([
                            html.H2('.........', style={...........}),
                        dcc.Dropdown(.....................)
                    ]),
#Second Inner division for adding 2 inner divisions for 2 output graphs
#TASK 2.3: Add two empty divisions for output inside the next inner division.
                    html.Div([
                
                        html.Div([ ], id='........'),
                        html.Div([ ], id='.........')
                    ], style={'.........}),

    ])
    #outer division ends

])
#layout ends
#TASK 2.4: Add the Ouput and input components inside the app.callback decorator.
#Place to add @app.callback Decorator
@app.callback([Output(component_id=.........., component_property=..........),
               Output(component_id=.........., component_property=..........)],
               [Input(component_id=.........., component_property=..........),
                Input(component_id=.........., component_property=..........)])

   
#TASK 2.5: Add the callback function.
#Place to define the callback function .
def reg_year_display(input_region,input_year):
    
    #data
   region_data = df[df['Region'] == input_region]
   y_r_data = region_data[region_data['Year']==input_year]
    #Plot one - Monthly Average Estimated Fire Area
   
   est_data = .........................
   fig1 = px.pie(.............., title="{} : Monthly Average Estimated Fire Area in year {}".format(input_region,input_year))
   
     #Plot two - Monthly Average Count of Pixels for Presumed Vegetation Fires
   veg_data = .............................
   fig2 = px.bar(..............., title='{} : Average Count of Pixels for Presumed Vegetation Fires in year {}'.format(input_region,input_year))
    
   return [.......,
            ......... ]

if __name__ == '__main__':
    app.run_server()