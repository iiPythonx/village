# Copyright (c) 2025 iiPython

# Modules
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from camp.config.schema import CabinSchema

# Initialization
class App(FastAPI):
    config: CabinSchema

app = App()

# Routing
@app.get("/config")
async def route_config() -> JSONResponse:
    return JSONResponse({
        "code": 200,
        "data": {
            "region": app.config.region,
            "contact": app.config.contact.serialize()
        }
    })
