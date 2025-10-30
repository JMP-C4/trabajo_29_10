from flask import Blueprint, jsonify, request
from inventario.app import db
from inventario.models.producto import Producto
from flask_paginate import get_page_args

productos_bp = Blueprint("productos", __name__)

@productos_bp.route("/", methods=["POST"])
def crear_producto():
    data = request.get_json()
    producto = Producto(nombre=data["nombre"], precio=data["precio"], stock=data["stock"])
    db.session.add(producto)
    db.session.commit()
    return jsonify({"message": "Producto creado", "id": producto.id}), 201

@productos_bp.route("/", methods=["GET"])
def listar_productos():
    page, per_page, _ = get_page_args(page_parameter="page", per_page_parameter="per_page")
    productos = Producto.query.paginate(page=page, per_page=per_page, error_out=False)
    data = [{"id": p.id, "nombre": p.nombre, "precio": p.precio, "stock": p.stock} for p in productos.items]
    return jsonify(data), 200

@productos_bp.route("/<int:id>/stock", methods=["PUT"])
def actualizar_stock(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    data = request.get_json()
    producto.stock = data["stock"]
    db.session.commit()
    return jsonify({"message": "Stock actualizado"}), 200

@productos_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "No existe"}), 404
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"message": "Eliminado correctamente"}), 200
