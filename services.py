import json
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models import DID
from schemas import DIDCreate

def create_did(db: Session, did_data: DIDCreate):
    existing_did = db.query(DID).filter(DID.did == did_data.did).first()
    if existing_did:
        raise ValueError(f"DID '{did_data.did}' already exists.")
    
    db_did = DID(
        did=did_data.did,
        controller=did_data.controller,
        document=json.dumps(did_data.document),
    )
    db.add(db_did)
    db.commit()
    db.refresh(db_did)
    return db_did

def get_did(db: Session, did_id: int):
    db_did = db.query(DID).filter(DID.id == did_id).first()
    if db_did:
        # Deserializar el documento de JSON a un diccionario
        db_did.document = json.loads(db_did.document)
    return db_did

def delete_did(db: Session, did_id: int):
    db_did = db.query(DID).filter(DID.id == did_id).first()
    if db_did:
        db.delete(db_did)
        db.commit()
    return db_did
