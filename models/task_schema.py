from pydantic import BaseModel

class Task(BaseModel):
    titulo: str
    descricao: str
    prioridade: int
    finalizada: bool = False