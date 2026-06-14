from dash import Output, Input, html
from services.databricks_svc import db_service
from ui.components import build_data_grid

def register_callbacks(app):
    @app.callback(
        Output("grid-container", "children"),
        Input("load-btn", "n_clicks"),
        Input("table-path-input", "value"),
        prevent_initial_call=True
    )
    def handle_table_query(n_clicks, table_path):
        if not table_path or len(table_path.split(".")) != 3:
            return html.Div("Invalid Format. Please input a complete dot-separated path (catalog.schema.table).", style={"color": "orange"})
            
        try:
            # Query backend data wrapper
            df = db_service.fetch_unity_catalog_table(table_path)
            
            if df.empty:
                return html.Div(f"Query executed successfully, but target table '{table_path}' contains zero records.")
            
            # Construct optimized AG Grid frontend payload
            return build_data_grid(df, grid_id="uc-production-grid")
            
        except Exception as e:
            # Production practice: Log full traceback internally, return sanitized UI alert
            return html.Div(f"Database Query Error: {str(e)}", style={"color": "#dc2626", "fontWeight": "bold"})