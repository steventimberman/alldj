import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

title_style = {
    "position": "fixed",
    "top": "15%",
    "left": "20%",
    "transform": "translate(-50%, -50%)"
}

centered = {
    "position": "fixed",
    "top": "50%",
    "left": "50%",
    "transform": "translate(-50%, -50%)"
}

centered_top = {
    "position": "fixed",
    "top": "25%",
    "left": "50%",
    "transform": "translate(-50%, -50%)"
}

centered_bottom = {
    "position": "fixed",
    "top": "75%",
    "left": "50%",
    "transform": "translate(-50%, -50%)"
}

def center_wraper(body):
    return dbc.Container(
        [
            dbc.Row(
                [
                    body
                ], style=centered
            )
        ], fluid=True
    )

def center_wraper_two_bodies(title, body1, body2):
    return dbc.Container(
        [
            dbc.Row(
                [
                    title
                ], style=title_style
            ),
            dbc.Row(
                [
                    body1
                ], style=centered_top
            ),
            dbc.Row(
                [
                    body2
                ], style=centered_bottom
            )
        ], fluid=True
    )

def center_item(item):
        return dbc.Row(
            dbc.Col([html.Div(item)])
        )

