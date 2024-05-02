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


# Path Variable 
# Receiving Data From Front-End to the Back-End through Path Variable 
@app.get("/getrollno/{rollNo}")
def getRollNo(rollNo):
    print("The Roll No of Muhammad Afzal (Student of Web Development) is", rollNo)
    return rollNo 

# Query Parameter 
# Receiving Data From Front-End to the Back-End through Query Parameter

@app.get("/getfromdata")
def getRollNo(userName:str, rollNo:str):
    print("Student Name is", userName, "&", "Student Roll no is", rollNo)
    return "Students Addmissions form"


def start():
    uvicorn.run("students_crud.main:app",host="127.0.0.1", port=8181, reload=True)