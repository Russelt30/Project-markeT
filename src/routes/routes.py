from src.controllers.controller import *
from src.controllers.errors import NotFoundController

routes = {
    "index_route": "/",
    "index_controller": IndexController.as_view("index"),
    "delete_route": "/delete/product/<int:code>",
    "delete_controller": DeleteProductController.as_view("delete"),
    "update_route": "/update/product/<int:code>",
    "update_contoller": UpdateProductController.as_view("update"),
    # rutas category
    "create_route": "/create/category/",
    "create_controller": CreateCategoriesController.as_view("category"),
    "eliminar_route": "/delete/category/<int:id>",
    "eliminar_controller": DeleteCategoriesController.as_view("eliminar"),
    "not_found_route": 404,
    "not_found_controller": NotFoundController.as_view("not_found"),
}
