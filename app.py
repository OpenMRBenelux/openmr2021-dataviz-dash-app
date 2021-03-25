# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.graph_objs as go
import os
import pandas as pd
import numpy as np


# ---------------
# Prepare data
# ---------------

# Grab data from CSV file and divide into arrays
data_dir = 'data'
tsnr_csv = os.path.join(data_dir, 'tsnr.csv')
df_tsnr = pd.read_csv(tsnr_csv)
dat1 = df_tsnr['brain'].dropna().to_numpy()
dat2 = df_tsnr['gm'].dropna().to_numpy()
dat3 = df_tsnr['wm'].dropna().to_numpy()
dat4 = df_tsnr['csf'].dropna().to_numpy()

# Create empty Plotly graph (updated in the relevant callback)
fig3 = go.Figure()

# Create options for dropdown
all_options = ['box', 'violin']
sub_opts = [{'label': opt, 'value': opt} for opt in all_options]


# ---------------
# Create app
# ---------------

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[
                    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
                ])
server = app.server


# ---------------
# App layout
# ---------------

main_md = dcc.Markdown('''The tools are out there for researchers to publish their data and results in rich online formats that offer accessibility, interaction and exploration.
Yet, we still see a majority of standard plots and images in PDF format.
In this demo, we will explore the possibilities offered by Python, Plotly and Dash to make your research outputs interactive and future-aware!
''')

app.layout = html.Div([
    html.Div(
        html.Img(src="/assets/section_header.png", width="70%"),
        style={ 'textAlign': 'center'}
    ),
    html.Br(),
    html.H1(
        children='From zero to interactivity in a Dash!',
        style={
            'textAlign': 'center',
        }
    ),
    html.Br(),
    html.Div([
        main_md,],
        style={
            'marginLeft': '5%',
            'maxWidth': '90%',
        }
    ),
    html.Br(),
    html.Div([
        dbc.Row([
            dbc.Col([
                html.H4(
                    children='Interactive tSNR plots',
                    style={
                        'textAlign': 'center',
                    }
                ),
                html.Br(),
                html.P('Select a type of chart:'),
                dcc.Dropdown(
                    id='drop_plot_options',
                    options=sub_opts,
                    value='box'
                ),
                html.Br(),
                html.H6(
                    children='Interactive tSNR chart',
                    id='heading3',
                    style={
                        'textAlign': 'center',
                    }
                ),
                dcc.Graph(figure=fig3, id='fig3')
                ], width={"size": 6, "offset": 0}
            ),
            dbc.Col([
                html.H4('Finger Tapping Task Map', style={'textAlign': 'center'}),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H6('A motor contrast that is visible and interactively explorable in three dimensions', style={'textAlign': 'center'}),
                html.Iframe(id='task_map1', src='/assets/statmap_viewer.html', style={'border': 'none', 'width': '100%', 'height': 500}),   
                # html.Iframe(id='task_map2', src='/assets/surface_viewer.html', style={'border': 'none', 'width': '100%', 'height': 500}),   
                ], width={"size": 6, "offset": 0}
            ),
        ]),
    ])
],
style={
    'marginBottom': 25,
    'marginTop': 50,
    'marginLeft': '5%',
    'maxWidth': '90%'
})



# ---------------
# App callbacks
# ---------------

# Callback for updating the box/violin plot
@app.callback(
    Output('fig3', 'figure'),
    [Input('drop_plot_options', 'value')]
)
def update_plot(plot_option):
    colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02']
    layout = go.Layout(
        yaxis = dict(title = 'Temporal signal-to-noise ratio (tSNR)', range=[-20, 250]),
        xaxis=dict(title='Tissue masks'),
        margin={'t': 0},
    )
    fig3 = go.Figure(layout=layout)
    if plot_option == 'box':
        fig3.add_trace(go.Box(y=dat1, line_color=colors[0], name='Brain'))
        fig3.add_trace(go.Box(y=dat2, line_color=colors[1], name='GM'))
        fig3.add_trace(go.Box(y=dat3, line_color=colors[2], name='WM'))
        fig3.add_trace(go.Box(y=dat4, line_color=colors[3], name='CSF'))
        heading = 'koek'
    else:
        fig3.add_trace(go.Violin(y=dat1, line_color=colors[0], name='Brain'))
        fig3.add_trace(go.Violin(y=dat2, line_color=colors[1], name='GM'))
        fig3.add_trace(go.Violin(y=dat3, line_color=colors[2], name='WM'))
        fig3.add_trace(go.Violin(y=dat4, line_color=colors[3], name='CSF'))
        fig3.update_traces(orientation='v', side='positive', width=1, box_visible=True, points=False)
        fig3.update_layout(xaxis_showgrid=True, yaxis_showgrid=True, xaxis_zeroline=False)
    return fig3

# Callback for updating heading based on selected
@app.callback(
     Output('heading3','children'),
    [Input('fig3', 'clickData')]
)
def reset_sub_tsnr_info(clickData): 
    if clickData is None:
        raise PreventUpdate
    else:
        curves = ['Brain', 'GM', 'WM', 'CSF']
        selected_trace = curves[clickData['points'][0]['curveNumber']]
        new_heading = 'Interactive tSNR chart (selected data = ' + selected_trace + ')' 
    return new_heading


# ---------------
# Run app
# ---------------
if __name__ == '__main__':
    app.run_server(debug=True)