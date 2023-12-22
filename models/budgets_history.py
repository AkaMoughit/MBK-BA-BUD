from datetime import datetime, date
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date, Boolean, Float, TIMESTAMP, ForeignKey,DateTime
from database import Base
from typing import Optional
from datetime import datetime,date


class BudgetHistory(Base):
    __tablename__ = "budgets_history"

    budgets_history_id = Column(Integer, primary_key=True, index=True)
    budgets_categories_id = Column(Integer)
    type = Column(Boolean)
    amount = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

class BudgetHistoryBase(BaseModel):
    budgets_categories_id: int
    type: bool
    amount: float
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]