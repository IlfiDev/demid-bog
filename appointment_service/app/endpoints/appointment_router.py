from uuid import UUID
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Body
from app.services.appointments_service import AppointmentsService
from app.models.appointments import Appointments
appointment_router = APIRouter(prefix='/appointment', tags=['Appointment'])

@appointment_router.get('/')
def get_appointment(appointments_service: AppointmentsService = Depends(AppointmentsService)) -> list[Appointments]:
    return appointments_service.get_appointment()

@appointment_router.post('/create')
def create_appointment(appointment_id: UUID, creation_date: datetime, appointment_date: datetime, name: str,
                       appointments_service: AppointmentsService = Depends(AppointmentsService)) -> Appointments:
    try:
        appointment = appointments_service.create_appointment(appointment_id = appointment_id, creation_date = creation_date , appointment_date = appointment_date, name = name)
        return appointment.model_dump()
    except KeyError:
        raise HTTPException(400)
    except ValueError:
        raise HTTPException(400)

@appointment_router.post('/{id}/get')
def get_appointment_by_id(id: UUID, appointments_service: AppointmentsService = Depends(AppointmentsService)) -> Appointments:
    return appointments_service.get_appointment_by_id(id)

@appointment_router.post('/{id}/finish')
def finish_appointment(id: UUID, appointments_service: AppointmentsService = Depends(AppointmentsService)) -> Appointments:
    try:
        appointment = appointments_service.finish_appointment(id)
        return appointment.model_dump()
    except KeyError:
        raise HTTPException(404, f'Appointment with id={id} not found')
    except ValueError:
        raise HTTPException(400, f'Appointment with id={id} can\'t be finished')

@appointment_router.post('/{id}/cancel')
def cancel_appointment(id: UUID, appointments_service: AppointmentsService = Depends(AppointmentsService)) -> Appointments:
    try:
        appointment = appointments_service.cancel_appointment(id)
        return appointment.model_dump()
    except KeyError:
        raise HTTPException(404, f'Appointment with id={id} not found')
    except ValueError:
        raise HTTPException(400, f'Appointment with id={id} can\'t be canceled')

@appointment_router.post('/{id}/appoint')
def set_trainer(
    id: UUID,
    trainer_id: UUID = Body(embed=True),
    appointments_service: AppointmentsService = Depends(AppointmentsService)) -> Appointments:
    try:
        appointment = appointments_service.set_trainer(id, trainer_id)
        return appointment.model_dump()
    except KeyError:
        raise HTTPException(404, f'Appointment with id={id} not found')
    except ValueError:
        raise HTTPException(400) 
