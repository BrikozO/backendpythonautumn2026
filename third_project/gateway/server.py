from fastapi import FastAPI

from third_project.gateway.api import notify

app = FastAPI()

app.include_router(notify.router)
