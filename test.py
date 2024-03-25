from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()
@app.get("/car",status_code=200,tags=["about car"])
def get_car():
    return {"output":"success"}
client =TestClient(app)
def test_hello():
    response = client.get("/car")
    assert response.status_code == 200, "Status:400"
    assert response.json()["output"] == "success", "Not success"
    
    





