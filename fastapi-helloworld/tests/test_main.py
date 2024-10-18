from fastapi_helloworld.main import app
from fastapi.testclient import TestClient

client:TestClient = TestClient(app=app)

def test_base_path():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World !"
    

def test_piaic_path():
    response = client.get("/piaic")
    assert response.status_code == 200
    assert response.json() == {"organization" : "PIAIC"}

