import dash
import plotly.express as px
import pandas as pd
import plotly
import plotly.graph_objs as go
import csv
import os
from dash import html, dcc
from datetime import datetime, timedelta
from dash.dependencies import Output, Input, State
from config import getFunctionConfig
from checkStatus import checkStatusOK
import csv_helper
from logsHelper import writeOverallStatusLog
from emailer import email_alert



app = dash.Dash(__name__)


green_button_style = {'background-color': 'green',
                      'color': 'black',
                      'height': '100px',
                      'width': '150px',
                      'margin-top': '50px',
                      'margin-left': '50px'}

red_button_style = {'background-color': 'red',
                    'color': 'white',
                    'height': '100px',
                    'width': '150px',
                    'margin-top': '50px',
                    'margin-left': '50px'}

grey_button_style = {'background-color': 'grey',
                      'color': 'black',
                      'height': '100px',
                      'width': '150px',
                      'margin-top': '50px',
                      'margin-left': '50px'}


# Layout for monitoring dashboard
app.layout = html.Div(children=[
    html.H1(children='QUB Editotron 3000: Monitoring & Metrics'),
    html.Div(id='live-update-buttons', style={"border":"2px black solid"}),
    html.H2('Number of Active Links over Time'),
    dcc.Graph(id="live-graph"),
    dcc.Interval(
        id='interval-component',
        interval=30*1000, # in milliseconds
        n_intervals=0
    ),
    html.Button('View Logs', id='view-logs', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Click to view logs')
    
])



# Plot graph of number of active links against time
# Date is read from CSV file
@app.callback(
    Output("live-graph", "figure"), 
    [Input('interval-component', 'n_intervals')])

def display_graph(n_intervals):
    
    # Read the CSV file
    df = pd.read_csv('overallStatus.csv')

    # Plot and return the graph
    fig = px.line(df, x='datetime', y='activelinks')    
    return fig



# Read what functions are available to the editor from config
# Test if the link is live
# Green if live, Red if down
@app.callback(Output('live-update-buttons', 'children'),
              Input('interval-component', 'n_intervals'))
def update_buttons(n):
    
    # Array to hold status of function links
    buttons = []
    # Count live links and down links, display metric to user
    liveEndPointCount = 0
    downEndPointCount = 0

    # Get the functions available to editor
    functions = getFunctionConfig("all")['Functions']
    for editorFunction in functions:
        links = get_links(editorFunction)
        
        datetimeNow = datetime.now()
        
        for link in links:
            # Check Status of links
            # Append buttons to array
            if checkStatusOK(link):
                buttons.append(makeStatusButton(editorFunction['name'], link, green_button_style))
                liveEndPointCount = liveEndPointCount + 1
            else:
                buttons.append(makeStatusButton(editorFunction['name'], link, red_button_style))
                email_alert("Problem with " + link, "There is a problem with this service.")
                downEndPointCount = downEndPointCount + 1
    
    # Text to display number of active links to user
    buttons.insert(0,html.H2('Current status: ' + str(liveEndPointCount) + " live services out of " + str(liveEndPointCount + downEndPointCount) + " total."))
    
    # Write status to CSV and log file
    csv_helper.writeToOverallStatusCSV(liveEndPointCount)
    writeOverallStatusLog(str(liveEndPointCount))
    return buttons


# Make status buttons
def makeStatusButton(name, link, statusStyle):
    return html.Button(name 
                        + " : Live / Uptime:" 
                        + csv_helper.get_uptime_last_hour(link) 
                        + "%" 
                        + " / Average response time:" 
                        + csv_helper.get_average_response_time_last_hour(link) 
                        + "s", id=link, n_clicks=0,style=statusStyle)


# Get links as array from config
def get_links(editorFunction):
    links = []
    links.append(editorFunction['link1'])
    links.append(editorFunction['link2'])
    links.append(editorFunction['link3'])
    return links


# View log file
@app.callback(
    Output('container-button-basic', 'children'),
    Input('view-logs', 'n_clicks')
)
def view_logs(n_clicks):
    os.startfile('logs.txt')
    return 'Logs opened'


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port='80')