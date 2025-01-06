from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from schemas import DIDCreate, DIDResponse
from services import create_did, get_did, delete_did

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "API de Identificadores Descentralizados (DIDs)"}

@app.post("/dids/", response_model=DIDResponse)
def create_new_did(did: DIDCreate, db: Session = Depends(get_db)):
    try:
        return create_did(db, did)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))  # Devuelve un error 400 (Bad Request)
    
@app.get("/dids/{did_id}", response_model=DIDResponse)
def read_did(did_id: int, db: Session = Depends(get_db)):
    db_did = get_did(db, did_id)
    if not db_did:
        raise HTTPException(status_code=404, detail="DID not found")
    return db_did

@app.delete("/dids/{did_id}")
def delete_existing_did(did_id: int, db: Session = Depends(get_db)):
    db_did = delete_did(db, did_id)
    if not db_did:
        raise HTTPException(status_code=404, detail="DID not found")
    return {"message": f"DID {did_id} deleted successfully"}
