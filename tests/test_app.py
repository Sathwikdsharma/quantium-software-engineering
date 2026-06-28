from app import app
from dash import dcc, html

def test_app_exists():
    assert app is not None

def test_layout_exists():
    assert app.layout is not None

def test_components_exist():
    layout = app.layout.children

    graph_found = False
    dropdown_found = False

    for component in layout:

        # Graph at top level
        if isinstance(component, dcc.Graph):
            graph_found = True

        # Dropdown inside Div
        if isinstance(component, html.Div):
            for child in component.children:
                if isinstance(child, dcc.Dropdown):
                    if child.id == "region-dropdown":
                        dropdown_found = True

    assert graph_found
    assert dropdown_found