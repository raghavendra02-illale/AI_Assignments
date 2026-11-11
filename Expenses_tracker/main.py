
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator


app = FastAPI(title="My Expense Manager")


# Allow frontend requests during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Store expense records
expense_records = {}
expense_id = 1


# Expense details
class Expense(BaseModel):
    description: str
    amount: float = Field(gt=0)
    category: str

    @field_validator("description", "category")
    @classmethod
    def check_text(cls, value):
        if not value.strip():
            raise ValueError("This field cannot be empty")

        return value.strip()


# Open the main webpage
@app.get("/")
async def home_page():
    return FileResponse("index.html")


# Add a new expense
@app.post("/expenses", status_code=201)
async def create_expense(expense: Expense):
    global expense_id

    new_record = {
        "id": expense_id,
        **expense.model_dump()
    }

    expense_records[expense_id] = new_record

    expense_id += 1

    return {
        "message": "New expense saved successfully",
        "expense": new_record
    }


# Display all expense records
@app.get("/expenses")
async def show_expenses():
    return list(expense_records.values())


# Update an existing expense
@app.put("/expenses/{record_id}")
async def change_expense(record_id: int, expense: Expense):

    if record_id not in expense_records:
        raise HTTPException(
            status_code=404,
            detail="Expense record not found"
        )

    updated_record = {
        "id": record_id,
        **expense.model_dump()
    }

    expense_records[record_id] = updated_record

    return {
        "message": "Expense updated successfully",
        "expense": updated_record
    }


# Remove an expense
@app.delete("/expenses/{record_id}")
async def remove_expense(record_id: int):

    if record_id not in expense_records:
        raise HTTPException(
            status_code=404,
            detail="Expense record not found"
        )

    del expense_records[record_id]

    return {
        "message": "Expense removed successfully"
    }
