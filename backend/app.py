from typing import Final

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from piccolo.engine import engine_finder

from questions.routers import app_router


async def open_database_connection_pool() -> None:
    engine = engine_finder()
    await engine.start_connection_pool()


async def close_database_connection_pool() -> None:
    engine = engine_finder()
    await engine.close_connection_pool()


app: Final = FastAPI(
    title="Simple Quiz Application",
    on_startup=[open_database_connection_pool],
    on_shutdown=[close_database_connection_pool],
)

app.include_router(
    app_router,
    prefix="/questions",
    tags=["question"],
)


@app.get("/")
async def greeting() -> JSONResponse:
    return JSONResponse(
        content={"message": "Hello World!"},
        status_code=200
    )
