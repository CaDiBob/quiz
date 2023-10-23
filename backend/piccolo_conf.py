from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine
from config import settings


DB: PostgresEngine = PostgresEngine(
    config={
        "database": settings.postgres_db,
        "user": settings.postgres_user,
        "password": settings.postgres_password,
        "host": settings.postgres_host,
        "port": settings.postgres_port,
    }
)

APP_REGISTRY: AppRegistry = AppRegistry(
    apps=[
        "questions.piccolo_app",
    ]
)
