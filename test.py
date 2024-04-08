####################################################################################
# FastAPI Application and Test Case Explanation
####################################################################################

# Importing necessary modules from FastAPI for creating the app and testing.
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Initializing the FastAPI app.
app = FastAPI()

# Defining a GET endpoint '/car' with a 200 OK status code. The endpoint is tagged with "about car".
@app.get("/car", status_code=200, tags=["about car"])
def get_car():
    # The function simply returns a JSON response {"output": "success"}.
    return {"output": "success"}

# Instantiating the TestClient with the FastAPI app.
client = TestClient(app)

# Defining a test function to validate the '/car' endpoint.
def test_getcar():
    # Making a GET request to the '/car' endpoint using the TestClient.
    response = client.get("/car")
    
    # Asserting the response status code is 200. If not, returns "Status:400".
    assert response.status_code == 200, "Status:400"
    
    # Asserting the response body contains {"output": "success"}. If not, returns "Not success".
    assert response.json()["output"] == "success", "Not success"

# This setup demonstrates how to define a basic FastAPI application with a single endpoint
# and write a test case using FastAPI's TestClient to ensure the endpoint behaves as expected.

####################################################################################


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
    
    





