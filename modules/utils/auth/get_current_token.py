from fastapi import Security
from fastapi.security.api_key import APIKeyHeader

authorization_token_key = APIKeyHeader(name="Authorization", auto_error=False)


def get_current_token(authorization_token: str = Security(authorization_token_key)) -> str:
    return authorization_token