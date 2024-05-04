from uuid import UUID
from datetime import datetime

from app.models.appointments import Appointments, AppointmentStatuses
from app.repositories.db_appointments_repo import AppointmentsRepo
from app.repositories.trainers_repo import TrainersRepo

class AppointmentsService():
    appointments_repo: AppointmentsRepo
    trainers_repo: TrainersRepo
    
    def __init__(self) -> None:
        self.appointments_repo = AppointmentsRepo()
        self.trainers_repo = TrainersRepo()

    def get_appointment(self) -> list[Appointments]:
        return self.appointments_repo.get_appointment()
    
    def get_appointment_by_id(self, id: UUID) -> Appointments:
        return self.appointments_repo.get_appointment_by_id(id)
    
    def create_appointment(self, appointment_id: UUID, creation_date: datetime, appointment_date: datetime, name: str) -> Appointments:
        appointment = Appointments(id = appointment_id, name = name, creation_date = creation_date, appointment_date = appointment_date, status=AppointmentStatuses.CREATED)
        return self.appointments_repo.create_appointment(appointment)
    
    def activate_appointment(self, id: UUID) -> Appointments:
        appointment = self.appointments_repo.get_appointment_by_id(id)
        if appointment.status != AppointmentStatuses.CREATED:
            raise ValueError

        appointment.status = AppointmentStatuses.ACTIVATED
        return self.appointments_repo.set_status(appointment)
 
    def set_trainer(self, appointments_id, trainers_id) -> Appointments:
        appointment = self.appointments_repo.get_appointment_by_id(appointments_id)
        try:
            trainer = self.trainers_repo.get_trainer_by_id(trainers_id)
        except KeyError:
            raise ValueError
        appointment.trainer = trainer
        return self.appointments_repo.set_trainer(appointment)
    
    def finish_appointment(self, id: UUID) -> Appointments:
        appointment = self.appointments_repo.get_appointment_by_id(id)
        if appointment.status != AppointmentStatuses.ACTIVATED:
            raise ValueError

        appointment.status = AppointmentStatuses.DONE
        return self.appointments_repo.set_status(appointment)

    def cancel_appointment(self, id: UUID) -> Appointments:
        appointment = self.appointments_repo.get_appointment_by_id(id)
        if appointment.status == AppointmentStatuses.DONE:
            raise ValueError

        appointment.status = AppointmentStatuses.CANCELED
        return self.appointments_repo.set_status(appointment)