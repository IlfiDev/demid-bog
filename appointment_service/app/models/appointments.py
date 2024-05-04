import enum
from uuid import UUID

from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.trainers import Trainer

class AppointmentStatuses(enum.Enum):
    CREATED = 'created'
    ACTIVATED = 'activated'
    DONE = 'done'
    CANCELED = 'canceled'

class Appointments(BaseModel): 
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    creation_date: datetime
    appointment_date: datetime
    status: AppointmentStatuses
    trainer: Trainer | None = None