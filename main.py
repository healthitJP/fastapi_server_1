from fastapi import FastAPI

app = FastAPI(
    title="FastAPI_server_1",
    description="なにかにする予定のAPI",
    version="1.0.0",
    swagger_ui_parameters={"docExpansion": "none"},
)


@app.get("/")
def read_root():
    return {"Hello": "こんにちは"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
