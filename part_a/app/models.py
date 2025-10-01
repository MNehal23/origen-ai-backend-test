# part_a/app/models.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MachineOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class ConvergencePoint(BaseModel):
    seconds: int
    loss: float

class SimulationCreate(BaseModel):
    name: str
    machine_id: int

class SimulationOut(BaseModel):
    id: int
    name: str
    machine_id: int
    status: str
    created_at: datetime
    updated_at: datetime
