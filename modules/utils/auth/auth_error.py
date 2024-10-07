from fastapi import HTTPException


class AuthorizationException(HTTPException):
    """Если пользователь не авторизован"""
