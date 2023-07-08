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
        return RedirectResponse(
            url=routes[route]
            + (
                f"?code={request.query_params['code']}"
                if "code" in request.query_params
                else ""
            )
        )

    app.get(route)(func)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
