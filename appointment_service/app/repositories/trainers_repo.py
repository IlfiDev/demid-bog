from uuid import UUID

from app.models.trainers import Trainer

trainers: list[Trainer] = [
    Trainer(
        id=UUID('85db966c-67f1-411e-95c0-f02edfa5464a'),
        name='Laptev Ivan Alexandrovich'),
    Trainer(
        id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
        name='Zuev Andrey Sergeevich'),
    Trainer(
        id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
        name='Kudj Stanislav Alekseevich')
]
class TrainersRepo():
    def get_trainer() -> list[Trainer]:
        return trainers
    
    def get_trainer_by_id(self, id: UUID) -> Trainer:
        for t in trainers:
            if t.id == id:
                return t
        raise KeyError