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
    
    @classmethod
    def from_string(cls, string):
        try:
            int(string)
            return cls.INT
        except ValueError:
            pass
        
        if string.lower() in {'true', 'false'}:
            return cls.BOOL

        try:
            float(string)
            return cls.DOUBLE
        except ValueError:
            pass

        for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S"):  # Добавьте нужные форматы
            try:
                datetime.strptime(string, fmt)
                return cls.TIMESTAMP
            except ValueError:
                continue
            
        return cls.TEXT