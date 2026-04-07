from repositories.task_repository import *
from bson import ObjectId

def format_task(task):
    task["_id"] = str(task["_id"])
    return task

def create_task_service(task):
    result = create_task(task.model_dump())
    return {"message": "Tarefa criada", "id": str(result.inserted_id)}

def get_all_tasks_service():
    tasks = get_all_tasks()
    return [format_task(t) for t in tasks]

def get_task_by_id_service(task_id):
    try:
        task = get_task_by_id(task_id)
        if not task: return {"error": "Não encontrada"}
        return format_task(task)
    except:
        return {"error": "ID Inválido"}

def update_task_service(task_id, task):
    try:
        result = update_task(task_id, task.model_dump())
        if result.matched_count == 0: return {"error": "Não encontrada"}
        return {"message": "Tarefa atualizada"}
    except:
        return {"error": "ID Inválido"}

def delete_task_service(task_id):
    try:
        result = delete_task(task_id)
        if result.deleted_count == 0: return {"error": "Não encontrada"}
        return {"message": "Tarefa deletada"}
    except:
        return {"error": "ID Inválido"}