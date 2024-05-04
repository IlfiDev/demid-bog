from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.dialects.postgresql import UUID

from app.schemas.base_schema import Base
from app.models.appointments import AppointmentStatuses

class Appointments(Base):
    __tablename__ = 'appointments'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    creation_date = Column(DateTime, nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    status = Column(ENUM(AppointmentStatuses,create_type=False), nullable=False)
    trainer_id = Column(UUID(as_uuid=True), nullable=True) 
