from fastapi import APIRouter

from .application import application

apps = APIRouter()

apps.include_router(
    application,
    prefix='/app',
    tags=['应用管理']
)

