from config.database import tasks_collection
from bson import ObjectId

def create_task(task_dict):
    return tasks_collection.insert_one(task_dict)

def get_all_tasks():
    return list(tasks_collection.find())

def get_task_by_id(task_id):
    return tasks_collection.find_one({"_id": ObjectId(task_id)})

def update_task(task_id, task_dict):
    return tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": task_dict}
    )

def delete_task(task_id):
    return tasks_collection.delete_one({"_id": ObjectId(task_id)})