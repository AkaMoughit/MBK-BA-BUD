from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.budgets import Budget, BudgetBase
from models.budgets_categories import BudgetCategory, BudgetCategoryBase

from database import get_db
from models.budgets_history import BudgetHistory, BudgetHistoryBase

router = APIRouter(prefix="/budgets/history", tags=["Budgets_History"])

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_budgets_history(db: Session = Depends(get_db)):
    budgets_history = db.query(BudgetHistory).all()
    return budgets_history

@router.get("/{budgets_history_id}", status_code=status.HTTP_200_OK)
async def get_budgets_history_by_id(budgets_history_id: int, db: Session = Depends(get_db)):
    # Retrieve a specific budget category by ID from the database
    budgets_history = db.query(BudgetHistory).filter(BudgetHistory.budgets_history_id == budgets_history_id).first()

    # Check if the budget category exists, raise an exception if not found
    if not budgets_history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Budgets_Categories with id {budgets_history_id} not found")

    return budgets_history

@router.put("/{budgets_history_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_budgets_history(budgets_history_id: int, budgets_history: BudgetHistoryBase, db: Session = Depends(get_db)):
    budgets_history_data = budgets_history.dict()
    budgets_history_data["updated_at"] = datetime.now()

    db.query(BudgetHistory).filter(BudgetHistory.budgets_history_id == budgets_history_id).update(budgets_history_data)
    db.commit()

    return {"message": "Budgets_History updated successfully"}

@router.delete("/{budgets_history_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_budgets_history(budgets_history_id: int, db: Session = Depends(get_db)):
    db.query(BudgetHistory).filter(BudgetHistory.budgets_history_id == budgets_history_id).delete(synchronize_session=False)
    db.commit()
    return {"message": "Budgets_History deleted successfully"}

@router.get("/budgets/{budgets_categories_id}", status_code=status.HTTP_200_OK)
async def get_budgets_history_by_budget_id(budgets_categories_id: int, db: Session = Depends(get_db)):
    budgets_history = db.query(BudgetHistory).filter(BudgetHistory.budgets_categories_id == budgets_categories_id).all()
    return budgets_history

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_budgets_history(budgets_history: BudgetHistoryBase, db: Session = Depends(get_db)):
    budgets_history_data = budgets_history.dict()
    budgets_history_data["created_at"] = datetime.now()
    db_budgets_history = BudgetHistory(**budgets_history_data)
    db.add(db_budgets_history)
    db.commit()
    return {"message": "Budgets_History created successfully"}

@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_budgets_history_by_user_id(user_id: int, db: Session = Depends(get_db)):
    budget = db.query(Budget).filter(Budget.user_id == user_id).first()
    budgets_categories = db.query(BudgetCategory).filter(BudgetCategory.budget_id == budget.budget_id).first()
    budgets_history = db.query(BudgetHistory).filter(BudgetHistory.budgets_categories_id == budgets_categories.budgets_categories_id).all()

    # Check if any budget categories are associated with the specified budget ID, raise an exception if not found
    if not budgets_history or not budget or not budgets_categories:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"budgets_history with user_id {user_id} not found")
    return budgets_history