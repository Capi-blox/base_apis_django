# yourproject/utils/jwt_utils.py
import jwt
from datetime import datetime, timedelta
from django.conf import settings

class JWTError(Exception):
    pass

def create_jwt(payload: dict, exp_minutes: int | None = None) -> str:
    if exp_minutes is None:
        exp_minutes = getattr(settings, "JWT_EXP_MINUTES", 60)

    now = datetime.utcnow()
    exp = now + timedelta(minutes=exp_minutes)

    # Clonar payload para no modificar el original
    data = payload.copy()
    data.update({
        "iat": now,
        "exp": exp,
    })
    token = jwt.encode(data, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    # PyJWT >=2.0 devuelve str
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token

def decode_jwt(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
            options={"require": ["exp", "iat"]},
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise JWTError("Token expirado")
    except jwt.InvalidTokenError as e:
        raise JWTError(f"Token inválido: {e}")
