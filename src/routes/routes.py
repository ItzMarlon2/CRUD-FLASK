from src.controllers.controller import *
from src.controllers.errors import NotFoundController

routes ={
    "index_route": "/", "index_controller": IndexController.as_view("index"),
    "delete_route": "/delete_product/<int:code>", "delte_controller": DeleteProductController.as_view("delte"),
    "update_route": "/update_product/<int:code>", "update_controller": UpdateProductController.as_view("update"),
    "categories_route": "/create/categorie", "categories_controller": CreateCategoriesController.as_view("categories"),
    "not_found_route": 404, "not_found_controller": NotFoundController.as_view("not_found")
}