from fastapi import APIRouter
from models.task_schema import Task
from services.task_service import *

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
def list_tasks():
    return get_all_tasks_service()

@router.post("/")
def add_task(task: Task):
    return create_task_service(task)

@router.get("/{task_id}")
def get_task(task_id: str):
    return get_task_by_id_service(task_id)

@router.put("/{task_id}")
def edit_task(task_id: str, task: Task):
    return update_task_service(task_id, task)

@router.delete("/{task_id}")
def remove_task(task_id: str):
    return delete_task_service(task_id)