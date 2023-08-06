import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([html.H1("Hoopalytics",className="title text-center",

                                    )
                            ],
                           fluid=True
                           )


if __name__ == "__main__":
    app.run_server(debug=True)