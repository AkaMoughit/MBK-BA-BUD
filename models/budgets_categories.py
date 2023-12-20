from datetime import datetime, date
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date, Boolean, DECIMAL, TIMESTAMP, ForeignKey, DateTime, Float
from database import Base

class BudgetCategory(Base):
    __tablename__ = "budgets_categories"

    budgets_categories_id = Column(Integer, primary_key=True, index=True)
    budget_id = Column(Integer)
    budget_name = Column(String(255))
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    amount = Column(Float)
    remaining_amount = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class BudgetCategoryBase(BaseModel):
    budget_id: int
    budget_name: str
    start_at: date
    end_at: date
    amount: float
    remaining_amount: float
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime