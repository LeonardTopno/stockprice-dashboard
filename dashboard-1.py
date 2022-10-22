import dash

# --- For Layouts ---
from dash import dcc   # import dash_core_components as dcc
from dash import html  # import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

# --- For Callback ---
from dash.dependencies import Input, Output


app = dash.Dash()  # initializing dash app
df = px.data.stocks()  # reading stock price dataset


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


# Defining Layouts
app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Styling using html components',
            style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40}),
    dcc.Graph(id='line_plot', figure=stock_prices()),
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
    # print(dropdown_value)  # For Dev: to check which dropdown value has been selected
    fig = go.Figure([go.Scatter(x=df['date'], y=df['{}'.format(dropdown_value)],
                                line=dict(color='firebrick', width=4))])
    fig.update_layout(title='Stock Prices Over Time',
                      xaxis_title='Dates',
                      yaxis_title='Prices')
    return fig


if __name__ == '__main__':  # Dash is built on top of Flask
    app.run_server()
