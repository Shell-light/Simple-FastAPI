from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}












"""
endpoint - localhost/delete-user
GET - GET ANY INFORMATION
POST - CREATE SOMETHING
PUT - UPDATE
DELETE - DELETE SOMTHING
"""
