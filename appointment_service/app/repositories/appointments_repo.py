from uuid import UUID

from app.models.appointments import Appointments

appointments: list[Appointments] = []

class AppointmentsRepo():
    def __init__(self, clear: bool = False) -> None:
        if clear:
            appointments.clear()

    def get_appointment(self) -> list[Appointments]:
        return appointments
    
    def get_appointment_by_id(self, id: UUID) -> Appointments:
        for a in appointments:
            if a.id == id:
                return a
        raise KeyError

    def create_appointment(self, appointment: Appointments) -> Appointments:
        if len([a for a in appointments if a.id == appointment.id]) > 0:
            raise KeyError
        appointments.append(appointment)
        return appointment
    

    def set_status(self, appointment: Appointments) -> Appointments:
        for a in appointments:
            if a.id == appointment.id:
                a.status = appointment.status
            break
        return appointment

    def set_trainer(self, appointment: Appointments) -> Appointments:
        for a in appointments:
            if a.id == appointment.id:
                a.trainer = appointment.trainer
            break
        return appointment