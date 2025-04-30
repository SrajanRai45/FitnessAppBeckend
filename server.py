from fastapi import FastAPI , HTTPException 
from chat import responding
from database import add_entry , delete_data , update_data , get_data , alldata
from pydantic import BaseModel              # for request body models
from datetime import date



#createting fast api app
app = FastAPI()

class Entry(BaseModel):
    date: date
    value: str

class UpdateEntry(BaseModel):
    date: date
    new_value: str


@app.post("/add-entry")
def api_add_entry(entry: Entry):
    a = responding(entry.value)
    add_entry(entry.date, a)      # Calls your DB function
    return {"status": "entry added", "date": entry.date, "value": a}


@app.delete("/delete-entry/{entry_date}")
def api_delete_entry(entry_date: date):
    delete_data(str(entry_date))
    return {"status": "entry deleted", "date": entry_date}


@app.put("/update-entry")
def api_update_entry(update: UpdateEntry):
    a = responding(update.new_value)
    update_data(a, update.date)
    return {"status": "entry updated", "date": update.date, "new_value": a}


@app.get("/get-entry/{entry_date}")
def api_get_entry(entry_date: date):
    data = get_data(entry_date)
    if not data:
        raise HTTPException(status_code=404, detail="No data found")  # error handling
    result = data[0][0]
    return {"date": entry_date, "value": result}


@app.get("/all-data")
def api_all_data():
    return {"all_data": alldata()}





