from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings


def create_token(data: dict):
    encode_data = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_EXPIRATION_MINUTE)
    encode_data.update({"exp": expire})
    return jwt.encode(encode_data, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
        return payload
    except JWTError:
        return None