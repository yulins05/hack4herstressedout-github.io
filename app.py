from dash import Dash
from config.settings import settings
from ui.layout import get_layout
from callbacks import register_callbacks

# Instantiate Dash with underlying production WSGI Flask instance exposed
app = Dash(__name__, title="Unity Catalog Portal")
server = app.server 

# Load visual architecture layouts
app.layout = get_layout()

# Wire event reactive controllers
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(
        host="0.0.0.0", 
        port=settings.PORT, 
        debug=settings.DEBUG
    )