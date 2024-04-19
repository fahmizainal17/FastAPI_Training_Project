####################################################################################
# FastAPI Route Examples
####################################################################################

from fastapi import FastAPI

app = FastAPI()

# Basic item retrieval example
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

#.............................................................................#

# File processing example
@app.get("/process_file/{item_id}")
def process_file(item_id: int):
    return {"sender": item_id}

#..............................................................................##

# Root endpoint example
@app.get("/")
async def root():
    return {"Sender": "Fahmi Zainal"}

#..............................................................................#

# Greeting endpoint example
@app.get("/")
def say_hello():
    return {"output": "success"}

#.............................................................................#

# Data fetching example
# @app.get("/car/{car_id}")
# def read_db(car_id: int):
#     # Placeholder for database access logic
#     get_db()
#     car_info = (
#         dd.sql(f"SELECT * FROM car_price.csv WHERE car_id = {car_id}")
#         .fetchdf()
#         .to_dict("index")
#     )
#     return car_info

####################################################################################
# Notes on FastAPI Features
####################################################################################

# Data Validation with Pydantic:
# - Pydantic is utilized for data validation, such as converting values to strings as necessary.
# - For POST requests sending a JSON body or GET requests with parameters, data type validation is vital, covering both integers and strings.
# - The typing module can offer hints, including Union[str, None] for accommodating multiple types.
# - BaseModel from Pydantic facilitates detailed annotations, enabling specification of path parameters (e.g., Title:Blablabla) and query parameters (e.g., with max length).
# - Defines fields in the response body through Pydantic models.

# Class Configuration and Auto Schemas:
# - Include model configurations within classes to generate automatic schema documentation.

# Security:
# - Manages usernames for authentication purposes.

# Middleware:
# - Employ middleware to monitor and record the execution times of endpoints.

# Routers:
# - In cases of numerous endpoints, utilizing routers to organize them enhances structure and maintainability.(Folder them up)

# Metadata:
# - Incorporate metadata into APIs for enhanced documentation and informational clarity.

# Testing Endpoints:#
# - Endpoint testing is paramount for reliability assurance.
# - Thoroughly tested endpoints are less prone to failure, aiding in scalable development.
# - Stresses the significance of adopting a safety-first approach from the coding phase, despite the initial time investment it may require.

####################################################################################
# Docker Notes
####################################################################################

# Docker Concepts:
# - Layers: Docker images are made up of layers.
# - Image: A stack of layers.
# - Container: Created from an image, it includes code, OS, and packages.
# - Docker Daemon: Manages Docker processes.
# - The term "Distro" refers to the distribution of the Linux operating system used in the Docker image.

# Docker Hub and Python:
# - Utilizes Python images from Docker Hub for consistency across environments.
# - Distribution: The specific version of Python and OS used, e.g., python:3.9-slim-bullseye.

# Dockerfile Format:
# - Starts with specifying the Python image.
# - Copies the application files.
# - Copies the requirements file.
# - Sets the working directory.

# Basic Docker Commands:
# - To try Docker, navigate to the docker learning directory: `cd learn_docker`
# - Build a Docker image: `docker build -t hello_docker .`
# - List Docker images: `docker images`
# - Run a Docker container: `docker run hello_docker`
# - Check the status of containers: `docker ps -a`  # This command is used to inspect status.
# - Stop a container by ID: `docker stop <id>`
# - Start a container by ID: `docker start <id>`
# - Run a Docker container: `docker run hello_docker`

# Docker Registry:
# - A repository for Docker images, similar to GitHub for code. Includes Docker Hub and ECR (Elastic Container Registry).
# - Pushing images to a registry: `docker push <image_name>`

# Additional Tools:
# - DIVE: Tool for inspecting Docker images, useful for debugging. Requires installation.
# - VSCode Dev Containers: Offers real-time debugging within containers, but is not recommended for all workflows.

# Docker CLI Cheat Sheet and Docker Compose:
# - Basic Docker CLI commands and Docker Compose are essential for managing containers and facilitating communication between them.

####################################################################################
# Dockerfile Creation and Explanation
####################################################################################

# Using an official Python runtime as the parent image for consistent environments.
# Example: FROM python:3.9-slim-bullseye
# - "python:3.9-slim-bullseye" specifies the Python version and base OS distro (Debian Bullseye, slim variant).
# - Distro refers to the Linux distribution version used in the Docker image, balancing features, size, and security.

# Setting the working directory within the container to manage application files.
# Example: WORKDIR /app

# Copying the application files from the project directory to the container.
# Example: COPY . /app

# Installing dependencies from the requirements.txt file without caching to reduce image size.
# Example: RUN pip install --no-cache-dir -r requirements.txt

# Exposing a port for the container to make the application accessible.
# Example: EXPOSE 80
# - Adjust the exposed port to match your application's serving port.

# Defining environment variables within the container for configuration.
# Example: ENV NAME World

# Specifying the default command to execute when the container starts, such as running a Python application.
# Example: CMD ["python", "app.py"]
# - Replace "app.py" with the name of your application's main script.

# This Dockerfile template serves as a guideline for building Docker images for Python applications, emphasizing the importance of selecting an appropriate base image and managing dependencies and configurations for optimal container performance and security.

####################################################################################
