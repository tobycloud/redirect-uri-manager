#!/usr/bin/env python3

import json
import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

load_dotenv()

app = FastAPI()

with open("routes.json", "r") as file:
    routes = json.load(file)

for route in routes:

    async def func(request: Request):
        response_url = f"{routes[route]}?"
        for param in request.query_params:
            response_url += f"{param}={request.query_params[param]}&"

        return RedirectResponse(url=response_url)

    app.get(route)(func)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
