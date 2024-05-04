import traceback
from uuid import UUID
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.appointments import Appointments
from app.schemas.appointments import Appointments as DBAppointments
from app.repositories.trainers_repo import TrainersRepo

class AppointmentsRepo():
    db: Session
    trainer_repo: TrainersRepo

    def __init__(self) -> None:
        self.db = next(get_db())
        self.trainer_repo = TrainersRepo()

    def _map_to_model(self, appointment: DBAppointments) -> Appointments:
        result = Appointments.from_orm(appointment)
        if appointment.trainer_id != None:
            result.trainer = self.trainer_repo.get_trainer_by_id(
                appointment.trainer_id)
        
        return result
    
    def _map_to_schema(self, appointment: Appointments) -> DBAppointments:
        data = dict(appointment)
        del data['trainer']
        data['trainer_id'] = appointment.trainer.id if appointment.trainer != None else None
        result = DBAppointments(**data)

        return result
    
    def get_appointment(self) -> list[Appointments]:
        appointments = []
        for d in self.db.query(DBAppointments).all():
            appointments.append(self._map_to_model(d))
        return appointments
    
    def get_appointment_by_id(self, id: UUID) -> Appointments:
        appointment = self.db \
            .query(DBAppointments) \
            .filter(DBAppointments.id == id) \
            .first()

        if appointment == None:
            raise KeyError
        return self._map_to_model(appointment)

    def create_appointment(self, appointment: Appointments) -> Appointments:
        try:
            db_appointment = self._map_to_schema(appointment)
            self.db.add(db_appointment)
            self.db.commit()
            return self._map_to_model(db_appointment)
        except:
            traceback.print_exc()
            raise KeyError
        
    def set_status(self, appointment: Appointments) -> Appointments:
        db_appointments = self.db.query(DBAppointments).filter(
            DBAppointments.id == appointment.id).first()
        db_appointments.status = appointment.status
        self.db.commit()
        return self._map_to_model(db_appointments)

    def set_trainer(self, appointment: Appointments) -> Appointments:
        db_appointments = self.db.query(DBAppointments).filter(
            DBAppointments.id == appointment.id).first()
        db_appointments.trainer_id = appointment.trainer.id
        self.db.commit()
        return self._map_to_model(db_appointments)
    
