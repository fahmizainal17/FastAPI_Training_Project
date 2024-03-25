# FastAPI Training Project

## About The Project

The FastAPI Training Project is a Python-based project demonstrating the use of FastAPI for creating and managing web APIs with a focus on rapid development, data validation, and API testing. This project illustrates basic to intermediate concepts of FastAPI, including path operations, data validation with Pydantic, middleware usage, routing, and security features. It's designed to be a starting point for understanding how to build scalable, efficient, and secure web APIs with FastAPI.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python 3.6+
- FastAPI
- Uvicorn (ASGI server)

### Installation

1. Clone the repo
   ```
   git clone https://github.com/your_username_/FastAPI_Training_Project.git
   ```
2. Install required packages
   ```
   pip install fastapi uvicorn pytest
   ```

## Usage

This project consists of several key components detailed below:

### Main API (`main.py`)

- **Root Endpoint:** Demonstrates a basic path operation that returns a JSON response.

  ```python
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/")
  def say_hello():
      return {"output": "success"}
  ```

- **Commented Code Blocks:** Contains examples of more complex operations such as database interaction, data validation, and advanced path operations. These are currently commented out for simplicity but serve as a template for real-world applications.

### Testing (`test.py`)

- **API Testing:** Uses FastAPI's TestClient to perform endpoint testing, ensuring reliability and correctness of the API responses.

  ```python
  from fastapi import FastAPI
  from fastapi.testclient import TestClient

  app = FastAPI()

  @app.get("/car", status_code=200, tags=["about car"])
  def get_car():
      return {"output": "success"}

  client = TestClient(app)

  def test_hello():
      response = client.get("/car")
      assert response.status_code == 200, "Status:400"
      assert response.json()["output"] == "success", "Not success"
  ```

### Project Structure

- **`.gitignore`**: Specifies intentionally untracked files to ignore.
- **`LICENSE`**: Contains the license details for the project.
- **`README.md`**: The file you're reading, providing project information.
- **`main.py` & `test.py`**: The main FastAPI application and its tests.
- **`.pytest_cache` & `__pycache__`**: Folders for cached files and bytecode compiled by Python and pytest.

### Features

- FastAPI framework usage for rapid API development.
- Pydantic models for request and response data validation.
- Test-driven development with FastAPI's testing client.
- Middlewares, routing, and metadata management.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [TestClient](https://fastapi.tiangolo.com/tutorial/testing/)

---

This README serves as a guide to understanding the structure and functionality offered by the FastAPI Training Project, emphasizing key aspects of FastAPI development and testing.