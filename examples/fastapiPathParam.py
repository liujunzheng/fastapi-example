from fastapi import APIRouter

fastPathParam = APIRouter()


@fastPathParam.get('/getParam/{user_id}')
def get_param(user_id: int):
    return {
        "message": 'this is path param msg',
        "user_id": user_id
    }
