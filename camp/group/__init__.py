# Copyright (c) 2025 iiPython

# Modules
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from camp.config.schema import GroupSchema

# Initialization
class App(FastAPI):
    config: GroupSchema

app = App()

# Routing
@app.get("/config")
async def route_config() -> JSONResponse:
    return JSONResponse({
        "code": 200,
        "data": {
            "rooms": app.config.rooms,
            "allowed_cabins": app.config.allowed_cabins
        }
    })
