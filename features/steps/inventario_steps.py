from behave import given, when, then
from inventario.app import create_app

@given("un producto nuevo")
def step_given_producto(context):
    context.app = create_app()
    context.client = context.app.test_client()
    context.data = {"nombre": "Tablet", "precio": 900, "stock": 12}

@when("lo envío a la API")
def step_when_envio(context):
    context.response = context.client.post("/api/productos/", json=context.data)

@then("la respuesta debe ser 201")
def step_then_respuesta(context):
    assert context.response.status_code == 201
