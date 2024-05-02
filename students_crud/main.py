from fastapi import FastAPI
import uvicorn



app = FastAPI()

students = [{
    "userName":"Muhammad Afzal",
    "rollNo": 126016
},
            {
    "userName":"Mian Haroon",
    "rollNo": 126017
},
            {
                "userName":"Jawad Ahmad",
                "rollNo": 126018
            },
            {
                "userName":"Shaikh Zaid",
                "rollNo": 126019
            }
            ]

@app.get("/")
def getStudents():
    return students


def start():
    uvicorn.run("students_crud.main:app",host="127.0.0.1", port=8181, reload=True)