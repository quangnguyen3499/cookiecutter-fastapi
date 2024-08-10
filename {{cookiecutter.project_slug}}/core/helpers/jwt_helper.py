from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from configs.common_config import settings
from core.exceptions import NotAuthenticated

auth_scheme = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(request_token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    try:
        token = request_token.credentials
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALG])
        username: str = payload.get("sub")
        if username != "user":
            raise NotAuthenticated("Unauthenticated")
    except JWTError:
        raise NotAuthenticated("Unauthenticated")

    return {"username": username}
