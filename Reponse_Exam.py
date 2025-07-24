from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import List

app = FastAPI()

@app.get("/hello")
def hello():
    return "Hello world"

@app.get("/welcome")
def welcome( name = str):
    return (f"welcome {name}")

student_list = []

class students(Base):
    Reference: str
    FirstName: str
    LastName: str
    Age: int

@app.post("/students". statut_code=201)
def add_students(new_students: List[Students]):
    student_list.extend(new_students)
    return students_list

@app.get("/students")
def get_students():
    return students_list

