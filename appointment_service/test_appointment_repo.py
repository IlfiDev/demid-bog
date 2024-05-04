import pytest
from uuid import uuid4
from datetime import datetime
from pydantic import ValidationError
from app.models.trainers import Trainer
from app.models.appointments import Appointments, AppointmentStatuses

@pytest.fixture()
def any_trainer() -> Trainer:
    return Trainer(id=uuid4(), name='trainer')

def test_appointment_creation(any_trainer: Trainer):
    id = uuid4()
    name = 'name'
    date = datetime.now()
    status = AppointmentStatuses.DONE
    appointment = Appointments(id=id, name=name, creation_date=date, 
                               appointment_date=date,status=status, trainer=any_trainer)

    assert dict(appointment) == {'id': id, 'name': name, 'creation_date': date,
                                 'appointment_date': date, 'status': status,
                                 'trainer': any_trainer}

def test_appointment_type_required(any_trainer: Trainer):
    with pytest.raises(ValidationError):
        Appointments(id=uuid4(), date=datetime.now(),
                 status=AppointmentStatuses.ACTIVATED, trainer=any_trainer)

def test_appointment_appointment_date_required(any_trainer: Trainer):
    with pytest.raises(ValidationError):
        Appointments(id=uuid4(), name='str', creation_date = datetime.now(),
                 status=AppointmentStatuses.ACTIVATED, trainer=any_trainer)
        
def test_appointment_creation_date_required(any_trainer: Trainer):
    with pytest.raises(ValidationError):
        Appointments(id=uuid4(), name='str', appointment_date = datetime.now(),
                 status=AppointmentStatuses.ACTIVATED, trainer=any_trainer)

def test_appointment_status_required(any_trainer: Trainer):
    with pytest.raises(ValidationError):
        Appointments(id=uuid4(), date=datetime.now(),
                 name='str', trainer=any_trainer)