import dash
import dash_auth  # for authentication

import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output  # for interactivity


# authentication details
VALID_USERNAME_PASSWORD_PAIRS = [
    ['Rashika', 'Rash']
]
# access the application instance for deployment purposes and server name too
app = dash.Dash('auth')  # 'auth' for authentication in app
server = app.server  # for accessing server while deploying
# pass details into app
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
# authentication will be done on a browser once only because it will cache the credentials (clear cache/browsing history to re-enter credentials)
app.layout = html.Div([
    dcc.Input(id='my-id', value='Dash App', type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)