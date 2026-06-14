from dash import html, dcc

def get_layout() -> html.Div:
    return html.Div([
        html.Header([
            html.H1("Enterprise Data Portal", style={"margin": "0"}),
            html.P("Unity Catalog Operations Viewer", style={"margin": "5px 0 0 0", "opacity": "0.8"})
        ], style={
            "backgroundColor": "#1f2937", "color": "white", 
            "padding": "20px", "fontFamily": "Segoe UI, sans-serif"
        }),
        
        html.Main([
            html.Div([
                html.Label("Target Catalog Pointer:", style={"fontWeight": "600", "display": "block", "marginBottom": "5px"}),
                dcc.Input(
                    id="table-path-input", 
                    placeholder="catalog.schema.table",
                    type="text", 
                    style={"width": "400px", "padding": "8px", "borderRadius": "4px", "border": "1px solid #ccc"}
                ),
                html.Button(
                    "Query Catalog", 
                    id="load-btn", 
                    n_clicks=0, 
                    style={"padding": "9px 20px", "marginLeft": "10px", "cursor": "pointer", "fontWeight": "bold"}
                )
            ], style={"marginBottom": "25px", "padding": "20px", "backgroundColor": "#f9fafb", "borderRadius": "6px"}),
            
            dcc.Loading(
                id="loading-grid",
                type="dot",
                children=html.Div(id="grid-container")
            )
        ], style={"padding": "30px", "maxWidth": "1400px", "margin": "0 auto"})
    ])