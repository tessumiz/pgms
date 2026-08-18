from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="AI-Enabled Smart Power Grid Management System")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "PGMS API is running"}

@app.get("/api/infrastructure/substations")
def get_substations(db: Session = Depends(database.get_db)):
    substations = db.query(models.Substation).all()
    return substations
