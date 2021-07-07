from fastapi import APIRouter

application = APIRouter()


@application.get(
    '/list',
    summary='获取应用列表',
    description='查询所有应用列表'
)
def get_apps():
    return []


@application.get(
    '/{app_id}',
    summary='获取应用详情',
    description='获取应用详情信息'
)
def get_detail(app_id: int):
    return {
        "getDetail": app_id
    }


@application.post(
    '/create',
    summary='创建应用',
    description='根据业务线需求创建对应的应用'
)
def create_app():
    return {
        "created": True
    }


@application.put(
    '/{app_id}',
    summary='修改应用',
    description='修改应用配置信息'
)
def update_app(app_id: int):
    return {
        "update": app_id
    }


@application.delete(
    '/{app_id}',
    summary='删除应用',
    description='删除后不可恢复'
)
def delete_app(app_id: int):
    return {
        "delete": app_id
    }
