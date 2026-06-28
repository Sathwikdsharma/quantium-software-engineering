import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Read processed data
df = pd.read_csv("output.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f9",
        "padding": "30px",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "Quantium Software Engineering Dashboard",
            style={
                "textAlign": "center",
                "color": "#003366"
            }
        ),

        html.H3(
            "Impact of Pink Morsel Price Increase on Sales",
            style={
                "textAlign": "center",
                "color": "#555555"
            }
        ),

        html.Div([
            html.Label("Select Region:",
                       style={"fontWeight": "bold"}),

            dcc.Dropdown(
                id="region-dropdown",
                options=[
                    {"label": "All", "value": "All"},
                    {"label": "North", "value": "north"},
                    {"label": "South", "value": "south"},
                    {"label": "East", "value": "east"},
                    {"label": "West", "value": "west"},
                ],
                value="All",
                clearable=False,
                style={"width": "300px"}
            ),
        ], style={"marginBottom": "20px"}),

        dcc.Graph(id="sales-chart")
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-dropdown", "value")
)
def update_graph(selected_region):

    if selected_region == "All":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region}"
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Date",
        yaxis_title="Sales"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)