from uvicorn import run
from fastapi import FastAPI

from examples import examples
from apps import apps

app = FastAPI()

app.include_router(
    examples,
    prefix='/examples',
)

app.include_router(
    apps,
    prefix='/applications',
)

if __name__ == '__main__':
    run(
        'setup:app',
        host='0.0.0.0',
        port=9000,
        reload=True,
        debug=True,
        workers=1
    )
