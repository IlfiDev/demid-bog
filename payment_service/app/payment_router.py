from fastapi import APIRouter, status, HTTPException, Form, Header
from uuid import UUID
import requests
import logging
from keycloak import KeycloakOpenID

from app.check_info import paycheck_body,payment_info

appointment_router = APIRouter(prefix='/payment', tags=['Payment'])
LOGGER = logging.getLogger(__name__)


KEYCLOAK_URL = "http://keycloak:8080/"
KEYCLOAK_CLIENT_ID = "testClient"
KEYCLOAK_REALM = "testRealm"
KEYCLOAK_CLIENT_SECRET = "**********"

keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_URL,
                                  client_id=KEYCLOAK_CLIENT_ID,
                                  realm_name=KEYCLOAK_REALM,
                                  client_secret_key=KEYCLOAK_CLIENT_SECRET)

@appointment_router.post("/get_jwt_token")
async def login(username: str = Form(...), password: str = Form(...)):
    try:
        token = keycloak_openid.token(grant_type=["password"],
                                      username=username,
                                      password=password)
        global user_token
        user_token = token
        LOGGER.info("{username} got logged in")
        return token
    except Exception as e:
        print(e)
        LOGGER.info('{e}')
        raise HTTPException(status_code=400, detail="Не удалось получить токен")

def chech_for_role_test(token):
    try:
        token_info = keycloak_openid.introspect(token)
        if "test" not in token_info["realm_access"]["roles"]:
            raise HTTPException(status_code=403, detail="Access denied")
        return token_info
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token or access denied")

@appointment_router.get("/health", status_code=status.HTTP_200_OK)
async def service_alive(token: str = Header()):
    if (chech_for_role_test(token)):
        return {'message': 'service alive'}
    else:
        return "Wrong JWT Token"

@appointment_router.get('/')
def get_payment_info(token: str = Header()):
    try:
        if (chech_for_role_test(token)):
            LOGGER.info("got payment")
            return payment_info
        else:
            return "invalid JWT"
    except KeyError:
        raise HTTPException(400)

@appointment_router.get('/create/{id}')
def create_paycheck(id: UUID, token: str = Header()):
    try:
        if (chech_for_role_test(token)):
            paycheck = paycheck_body(info = requests.get)
            LOGGER.info("create paycheck with appointment id:{id}")
            return paycheck
        else:
            return "invalid JWT"
    except ValueError:
        raise HTTPException(400)
    except ConnectionError:
        raise HTTPException(502)
