from fastapi import APIRouter

from .examplePydantic import examplePdt
from .fastapiPathParam import fastPathParam

examples = APIRouter()

examples.include_router(
    examplePdt,
    prefix='/pdt'
)

examples.include_router(
    fastPathParam,
    prefix='/fast',
    tags=['fastAPI案例']
)
