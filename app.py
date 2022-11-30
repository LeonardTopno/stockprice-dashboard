import dash
import json 
# --- For Layouts ---
from dash import dcc   # import dash_core_components as dcc
from dash import html  # import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

import data_extract as de

# --- For Callback ---
from dash.dependencies import Input, Output


app = dash.Dash()  # initializing dash app



df = px.data.stocks()  # reading stock price dataset
#print("dataframe from stokcs\n", df)



tb_headers = de.tb_headers
# print("TB_HEADERS:", tb_headers)
period = list(de.period.keys())
# print("period:", list(period))

cells = [period, [0]*15, [1]*15, [3]*15, [6]*15]


# Defining a function for pre-interactive version of the dashboard
def stock_prices():
    """
    function for creating line chart showing Google Stock Prices over time
    """
    fig = go.Figure([go.Scatter(x=df['date'], y=df['GOOG'],
                                line=dict(color='firebrick', width=4), name='Google')
                     ])
    fig.update_layout(title='Prices over time',
                      xaxis_title='Dates',
                      yaxis_title='Prices')
    return fig

def get_table():
    fig = go.Figure(data = [go.Table(
    header=dict(values=tb_headers,
                    fill_color='paleturquoise',
                    align='left'),
    cells=dict(values=cells,
                fill_color='lavender',
                align='left')
    )])
    return fig #fig.show()


# Defining Layouts
app.layout = html.Div(id='parent', children=[
    html.H1(id='H2', children='S099 Forecast Analytical Dashboard',
            style={'textAlign': 'center', 'marginTop': 10, 'marginBottom': 20}),
    #dcc.Graph(id='line_plot', figure=stock_prices()),
    dcc.RadioItems(['Comm FC', 'Stat FC', 'Normal Demand'], "Comm FC", inline=True),
    dcc.Dropdown(id='items_dropdown',
                 options=[
                     {'label': 'All Items', 'value': 'All'},
                     {'label': '28953892', 'value': '28953892'},
                     {'label': '28953771', 'value': '28953771'},
                     {'label': '1004712', 'value': '1004712'},
                 ],
                 value='All'),
    dcc.Graph(id='forecast_table', figure=get_table()),

    dcc.Dropdown(id='dropdown',
                 options=[
                     {'label': 'Google', 'value': 'GOOG'},
                     {'label': 'Apple', 'value': 'AAPL'},
                     {'label': 'Amazon', 'value': 'AMZN'},
                 ],
                 value='GOOG'),
    dcc.Graph(id='bar_plot')
])


# Defining a Callback | Callbacks are followed by a function
@app.callback(Output(component_id='bar_plot', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])
def graph_update(dropdown_value):
    """
    function for creating line chart showing Google Stock Prices over time
    """
    # print(dropdown_value)  # For Dev: to check which dropdown value has been selected
    fig = go.Figure([go.Scatter(x=df['date'], y=df['{}'.format(dropdown_value)],
                                line=dict(color='firebrick', width=4))])
    fig.update_layout(title='Stock Prices Over Time',
                      xaxis_title='Dates',
                      yaxis_title='Prices')
    return fig


if __name__ == '__main__':  # Dash is built on top of Flask
    app.run_server(debug=True, threaded=True)
