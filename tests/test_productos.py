import pytest
from inventario.app import create_app, db
from inventario.models.producto import Producto

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client

def test_crear_producto(client):
    response = client.post("/api/productos/", json={"nombre": "Laptop", "precio": 1200, "stock": 10})
    assert response.status_code == 201

def test_listar_productos(client):
    client.post("/api/productos/", json={"nombre": "Mouse", "precio": 50, "stock": 20})
    response = client.get("/api/productos/")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_actualizar_stock(client):
    client.post("/api/productos/", json={"nombre": "Teclado", "precio": 70, "stock": 5})
    response = client.put("/api/productos/1/stock", json={"stock": 15})
    assert response.status_code == 200

def test_eliminar_producto(client):
    client.post("/api/productos/", json={"nombre": "Monitor", "precio": 300, "stock": 8})
    response = client.delete("/api/productos/1")
    assert response.status_code == 200
