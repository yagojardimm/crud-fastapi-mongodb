from fastapi import FastAPI
from routers.task_router import router

app = FastAPI(title="CRUD de Tarefas - Yago")

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "Online", "database": "MongoDB"}