import datetime
import random
from flask import Flask
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from admin_dashboard_helper import network_load, user_names, new_users, users_month, users_year, active_users, study_time

from admin_dashboard import *
from user_dashboard import *
from report_dashboard import *

# Initialize the Flask app
server = Flask(__name__)

# Initialize the Dash app
# app = dash.Dash(__name__, server=server, url_base_pathname='/admin_dashboard/', external_stylesheets=[dbc.themes.SLATE])


# Create the first Dash app for the admin dashboard
admin_dashboard = dash.Dash(
    __name__,
    server=server,
    url_base_pathname='/admin_dashboard/',
    external_stylesheets=[dbc.themes.SLATE]
)


user_dashboard = dash.Dash(
    __name__,
    server=server,
    url_base_pathname='/user_dashboard/',
    external_stylesheets=[dbc.themes.SLATE]
)

report_dashboard = dash.Dash(
    __name__,
    server=server,
    url_base_pathname='/report/',
    external_stylesheets=[dbc.themes.SLATE]
)



# Build App Layout
admin_dashboard.layout = html.Div([
    dbc.Card(
        dbc.CardBody([

            
            dbc.Row([
                dbc.Col(drawText_Admin_Dashbaord(), width=20),
            ], align='center'),


            html.Br(),


            dbc.Row([
                dbc.Col(drawFigure_Users_Month(), width=3.5),
            ], align='center'),


            html.Br(),
            

            dbc.Row([
                dbc.Col(drawFigure_Users_Year(), width=4),
                dbc.Col(drawFigure_Users_Active(), width=3),
                dbc.Col(drawFigure_Users_Study_Time(), width=5),
                
            ]),

            html.Br(),

            dbc.Row([
                dbc.Col(drawFigure_Users_New_Users(), width=5),
                dbc.Col(drawFigure_Users_Name(), width=4),
                dbc.Col(drawFigure_Up_Time(), width=3),
            ],align='center'),


            html.Br(),


            dbc.Row([
                dbc.Col(drawFigure_Network_load(), width=9),
            ], align='center'),
        ]), color='dark'
    )
])




user_dashboard.layout = html.Div([
    dbc.Card(
        dbc.CardBody([

            dbc.Row([
                dbc.Col(drawText_User_Dashbaord(), width=20),
            ], align='center'),


            html.Br(),
            
            dbc.Row([
                dbc.Col(drawFigure_Test_Insight(), width=3),
                dbc.Col(drawFigure_Users_Month(), width=5),
                dbc.Col(drawFigure_Correct_Incorrect(), width=4),

            ], align='center'),

            html.Br(),

            dbc.Row([
                dbc.Col(drawFigure_Average(), width=3),
                dbc.Col(drawFigure_User_activity(), width=3),
                dbc.Col(drawFigure_Leaderbaord(), width=5),

            ], align='center'),

            html.Br(),

        ]), color='dark'
    )
])


data = pd.DataFrame({
    'Time Taken (seconds)': [1, 3, 6, 7],
    'Points': [1, 0, 1, 0],  # 0 = Correct, 1 = Incorrect
})
data['Correct or Incorrect'] = data['Points'].map({0: 'Correct', 1: 'Incorrect'})

report_dashboard.layout = html.Div([
    dbc.Card(
        dbc.CardBody([

            dbc.Row([
                dbc.Col(drawText_Report_Dashbaord(), width=20),
            ], align='center'),


            html.Br(),
            
            dbc.Row([
                dbc.Col(drawFigure_Correct_incorrect(data), width=3),
                dbc.Col(drawFigure_Average_score_Report(data), width=3),
                dbc.Col(drawFigure_Time_Taken(data), width=3),
                dbc.Col(drawFigure_Leaderbaord_Report(), width=3),
            ], align='center'),

            html.Br(),



        ]), color='dark'
    )
])

# Run the Dash server
if __name__ == '__main__':
    server.run(debug=True, port=5000)