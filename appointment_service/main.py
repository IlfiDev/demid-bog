from fastapi import FastAPI
from app.settings import settings
from app.endpoints.appointment_router import appointment_router

app = FastAPI(title='Appointment Service')

app.include_router(appointment_router, prefix='/api')

"""
if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
"""