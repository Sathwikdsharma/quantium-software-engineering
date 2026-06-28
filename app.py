import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Read processed data
df = pd.read_csv("output.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase",
    annotation_position="top"
)

# Update axis labels
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales",
    template="plotly_white"
)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Quantium Software Engineering Dashboard"),
    html.H3("Impact of Pink Morsel Price Increase on Sales"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)