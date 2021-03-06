from typing import List

from app.db import init_db, get_session
from app.models import Form, FormBase

from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://gsus-register",
    "http://gsus-visualization",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()
    
    
@app.get("/app/v1/forms/{form_id}", response_model=Form)
def get_data(form_id:int, db: Session = Depends(get_session)):
    statement = select(Form).where(Form.id == form_id)
    form = db.exec(statement).first()
    return form

@app.get("/app/v1/forms", response_model=List[Form])
def get_data(db: Session = Depends(get_session)):
    statement = select(Form)
    form = db.exec(statement).all()
    return form

@app.post("/app/v1/forms")
def insert_data(form: FormBase, db: Session = Depends(get_session)):
    recieved_form = Form(
        name=form.name,
        last_name=form.last_name,
        age=form.age,
        position=form.position)
    db.add(recieved_form)
    db.commit()
    db.refresh(recieved_form)
    return recieved_form