from flask import request, render_template, redirect, flash
from flask.views import MethodView
from src.db import mysql


class IndexController(MethodView):
    # mostrar informacion db
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM products")
            data = cur.fetchall()
            cur.execute("SELECT * FROM categories")
            categories = cur.fetchall()
            return render_template(
                "public/index.html", data=data, categories=categories
            )

    def post(self):
        code = request.form["code"]
        name = request.form["name"]
        stock = request.form["stock"]
        value = request.form["value"]
        category = request.form["category"]

        # alias para conexion a bd
        # registrar productos
        with mysql.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO products(code, name, stock, value, id_category) values(%s, %s, %s, %s, %s)",
                    (code, name, stock, value, category),
                )
                cur.connection.commit()
                flash("El producto ha sido agregado correctamente", "success")
            except:
                flash("un error ha ocurrido", "error")
            return redirect("/")


class DeleteProductController(MethodView):
    def post(self, code):
        with mysql.cursor() as cur:
            try:
                cur.execute("DELETE FROM products WHERE code = %s", (code))
                cur.connection.commit()
                flash("Se ha eliminado el producto correctamente", "success")
            except:
                flash("un error ha ocurrido", "error")
            return redirect("/")


class UpdateProductController(MethodView):
    def get(self, code):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM products WHERE code = %s", (code))
            product = cur.fetchone()
            return render_template("public/update.html", product=product)

    def post(self, code):
        productCode = request.form["code"]
        name = request.form["name"]
        stock = request.form["stock"]
        value = request.form["value"]
        category = request.form["id_category"]

        with mysql.cursor() as cur:
            try:
                cur.execute(
                    "UPDATE products SET code = %s, name = %s, stock = %s, value = %s, id_category = %s WHERE code = %s",
                    (productCode, name, stock, value, category, code),
                )
                cur.connection.commit()  # guarde los datos
                flash("EL producto se ha actualizado correctamente", "success")
            except:
                flash("Un error ha ocurrido al actualizar el producto", "error")
            return redirect("/")


class CreateCategoriesController(MethodView):
    def get(self):
        with mysql.cursor() as cat:
            cat.execute("SELECT * FROM categories")
            dat = cat.fetchall()
            return render_template("public/categories.html", dat=dat)

    def post(self):
        id = request.form["id"]
        name = request.form["name"]
        description = request.form["description"]

        with mysql.cursor() as cat:
            try:
                cat.execute(
                    "INSERT INTO categories VALUES(%s, %s, %s)", (id, name, description)
                )
                cat.connection.commit()
                flash("La categoria se ha agregado correctamente", "success")
            except:
                flash("un error ha ocurrido", "error")
            return redirect("/")


class DeleteCategoriesController(MethodView):
    def post(self, id):
        with mysql.cursor() as cat:
            cat.execute("DELETE FROM categories WHERE id = %s", (id))
            cat.connection.commit()
            return redirect("/")
