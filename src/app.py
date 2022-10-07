from flask import Flask
from src.routes.routes import *

# inicializar app
app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="development")

# rutas de la aplicacion

app.add_url_rule(routes["index_route"], view_func=routes["index_controller"])
app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])
app.add_url_rule(routes["update_route"], view_func=routes["update_contoller"])

# rutas category

app.add_url_rule(routes["create_route"], view_func=routes["create_controller"])
app.add_url_rule(routes["eliminar_route"], view_func=routes["eliminar_controller"])

# ruta del error 404.
# registrar error y la vista
app.register_error_handler(routes["not_found_route"], routes["not_found_controller"])
