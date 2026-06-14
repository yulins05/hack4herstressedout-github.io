import dash_ag_grid as dag
import pandas as pd
from dash import html

def build_data_grid(df: pd.DataFrame, grid_id: str) -> dag.AgGrid:
    """Factory function generating an enterprise-ready Dash AG Grid."""
    column_defs = [{"field": col, "filter": True, "sortable": True} for col in df.columns]
    
    return dag.AgGrid(
        id=grid_id,
        rowData=df.to_dict("records"),
        columnDefs=column_defs,
        defaultColDef={
            "resizable": True, 
            "flex": 1, 
            "minWidth": 130,
            "floatingFilter": True # Sub-header inline column filtering
        },
        dashGridOptions={
            "pagination": True, 
            "paginationPageSize": 25,
            "rowSelection": "single"
        },
        style={"height": "600px", "width": "100%"},
        className="ag-theme-alpine" # Standard clean corporate theme
    )