from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import JWTError, jwt

import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
JWT_ALGORITHM = os.environ["JWT_ALGORITHM"]
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["JWT_ACCESS_TOKEN_EXPIRE_MINUTES"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", truncate_error=True)

def verify_password(plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(plain_password):
  return pwd_context.hash(plain_password)

def create_access_token(data: dict):
  payload = data.copy()
  expire = datetime.now(timezone.utc).replace(microsecond=0) + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
  payload.update({"exp": expire})
  encoded_jwt = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
  return encoded_jwt, expire.isoformat()

def get_payload(token: str):
  return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])