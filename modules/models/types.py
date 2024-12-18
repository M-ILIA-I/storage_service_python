from datetime import datetime
from sqlalchemy import Enum, Column, Integer, DateTime, func, Double, Boolean, Uuid, String, ForeignKey, UniqueConstraint, TIMESTAMP
from sqlalchemy.orm import relationship, Mapped, declarative_base
from modules.models.base_model import Base
import enum
import uuid


class TypeValue(enum.Enum):
    """
    int 
    bool 
    text
    double
    """
    INT = 1
    BOOL = 2
    TEXT = 3
    DOUBLE = 4
    TIMESTAMP = 5