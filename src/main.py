from fastapi import FastAPI

from error_handlers import register_errors_handlers
from routers import api_router

app = FastAPI()
register_errors_handlers(app)

app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)

