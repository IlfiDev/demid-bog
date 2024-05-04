import logging
from fastapi import FastAPI
from logging_setup import LoggerSetup
from app.payment_router import appointment_router
from prometheus_fastapi_instrumentator import Instrumentator
import os

app = FastAPI(title='Payment service', openapi_url="/api/payment/openapi.json", docs_url="/api/payment/docs")

app.include_router(appointment_router, prefix='/api/payment')


logger_setup = LoggerSetup()
# get logger for module
LOGGER = logging.getLogger(__name__)

Instrumentator().instrument(app).expose(app)


if __name__ == '__main__':
    import uvicorn
    LOGGER.info("--- start up App ---")
    PORT = 5000
    uvicorn.run(app, host='0.0.0.0', port=PORT)

