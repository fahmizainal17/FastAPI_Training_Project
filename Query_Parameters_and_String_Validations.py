### Query Parameters
# In FastAPI, query parameters are used to pass non-mandatory or optional information to the API via the URL. These parameters are typically used to refine the output or to specify certain kinds of data retrieval operations, like pagination or filtering. Query parameters are an essential part of RESTful APIs and provide flexibility in data retrieval requests.

# To define query parameters in FastAPI, you simply add them as function arguments to your endpoint functions. FastAPI automatically recognizes these arguments as query parameters if they are not part of the path parameters and not declared as request body.

# Here is a simple example to demonstrate the usage of query parameters:

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items1/")
async def read_items1(q: Optional[str] = None):
    if q:
        return {"item1": ["Item 1", "Item 2"], "query": q}
    return {"item1": ["Item 1", "Item 2"]}

# In this example, the `q` query parameter is optional, and it's used to filter or search the items based on the query string.

### String Validations
# FastAPI provides powerful tools for data validation using Pydantic models and Python's standard `typing` module. For strings specifically, you can enforce validations such as minimum and maximum lengths, regex patterns, and much more directly in the function signature using Pydantic's field functions or directly in the endpoint function's parameters.

# Here's how you can add validations to query parameters in FastAPI:


from fastapi import FastAPI, Query
from typing import Optional

@app.get("/items2/")
async def read_items2(
    q: Optional[str] = Query(
        None, 
        min_length=3, 
        max_length=50, 
        title="Query string",
        description="Query string for searching/filtering items. Must be between 3 and 50 characters."
    )
):
    if q:
        return {"items2": ["Item 1", "Item 2"], "query": q}
    return {"items2": ["Item 1", "Item 2"]}


# In this example, the query parameter `q` is validated to ensure it's between 3 and 50 characters in length. FastAPI uses these validation rules to validate the data before it hits your endpoint logic. If the validation fails, FastAPI automatically sends a detailed error response that describes the validation error, which is immensely helpful for debugging and for clients consuming the API.

# These features make it straightforward to build APIs that are both robust and easy to maintain, thanks to FastAPI's strong integration with Pydantic for data validation.

