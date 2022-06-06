import uvicorn
from fastapi import FastAPI

from api.v1.routes.main import router
from .config import settings

app = FastAPI()

app.include_router(router, prefix='/api')


if __name__ == '__main__':
    is_reload: bool = True
    if settings.ENV == 'production':
        is_reload = False
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT,
                log_level=settings.APP_LOG_LEVEL, reload=is_reload)
