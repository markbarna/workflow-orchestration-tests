import handlers
from airflow.models.taskinstance import TaskInstance
from handlers.base import BaseHandler
from typing import Callable, Type

def wrap_handler(handler_class: Type[BaseHandler]) -> Callable:
    def python_task(params: dict, ti: TaskInstance, **context):
        handler = handler_class(params)
        request = ti.xcom_pull(key="request")
        out_request = handler.handle(request)
        ti.xcom_push(out_request)
        return
    return python_task