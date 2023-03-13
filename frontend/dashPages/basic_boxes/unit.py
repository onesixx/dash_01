from dash import Dash, dcc, html
import dash_admin_components as dac
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State


view0= dcc.Slider(
           id='controlbar-slider',
           min=10, max=50, step=1, value=20
       )

view = dcc.Graph(
    id='box-graph',
    config=dict(displayModeBar=False),
    style={'width': '100%'}
)



# =============================================================================
# Dash App and Flask Server
# =============================================================================
app_dash = Dash(__name__)
# =============================================================================
# App Layout
# =============================================================================
#app_dash.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
app_dash.layout = [view0, view]
# =============================================================================
# Callback
# =============================================================================
# frontend.dashPages.tab_cards.callbacks.get_callbacks(app_dash)


# @app_dash.callback(
#     Output('box-graph', 'figure'),
#     [Input('controlbar-slider', 'value')])
# def update_box_graph(value):
#     # go.Figure()
#     return plot_scatter(value)
# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app_dash.run_server(debug=False)
