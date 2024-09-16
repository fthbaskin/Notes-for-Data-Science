from enum import Enum
from fastapi import FastAPI


app = FastAPI()


# Root path
@app.get("/")
async def read_root():
    return {"Hello": "World"}


# Path Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# Path parameters with type
@app.get('/get_specific_type/{item_id}')
async def get_specific_type(item_id: int):
    return {"item_id": item_id}


# Path parameters with specific value
class SpecificValue(str, Enum):
    value1 = "value1"
    value2 = "value2"


@app.get('/get_specific_value/{item_id}')
async def get_specific_value(item_id: SpecificValue):
    return {"item_id": item_id}
