# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# ---------------
# Style sheets
# ---------------
# external_stylesheets = [
#     'https://codepen.io/chriddyp/pen/bWLwgP.css',
#     {
#         'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
#         'rel': 'stylesheet',
#         'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
#         'crossorigin': 'anonymous'
#     }
# ]

# ---------------
# Prepare data
# ---------------

# img = datasets.fetch_localizer_button_task()['tmap']     
# view = plotting.view_img_on_surf(img, threshold='90%', surf_mesh='fsaverage')
# # view.save_as_html("pic1.html") 

main_md = dcc.Markdown('''The tools are out there for researchers to publish their data and results in rich online formats that offer accessibility, interaction and exploration. Yet, we still see a majority of standard plots and images in PDF format. In this demo, we will explore the possibilities offered by Python, Plotly and Dash to make your research outputs interactive and future-aware!''')
# Create card components to display on home page
card_access = [
    dbc.CardBody(
        [
            html.H5("Access", className="card-title"),
            html.P(
                "The BIDS-compatible rt-me-fMRI dataset is accessible via a GDPR-compliant data use agreement on DataverseNL...",
                className="card-text",
            ),
            dbc.Button("Access the dataset", color="light", href="/pages/access", external_link=True),
        ]
    ),
]

# ---------------
# Create app
# ---------------

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[
                    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
                ])
# app.config.suppress_callback_exceptions = True
server = app.server


# ---------------
# App layout
# ---------------



app.layout = html.Div([
    html.Div(
        html.Img(src="/assets/section_header.png", width="100%"),
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
            dbc.Col(dbc.Card(card_access, color="secondary", inverse=True)),
            dbc.Col(dbc.Card(card_access, color="info", inverse=True)),
            ],
            className="mb-4",
        ),
        ]
    )
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

# @app.callback(
#     Output(component_id='my-output', component_property='children'),
#     Input(component_id='my-input', component_property='value')
# )
# def update_output_div(input_value):
#     return 'Output: {}'.format(input_value)

# ---------------
# Run app
# ---------------

if __name__ == '__main__':
    app.run_server(debug=True)


