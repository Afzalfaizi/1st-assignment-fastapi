from fastapi import FastAPI
import uvicorn



app = FastAPI()

students = [{
    "userName":"Muhammad Afzal",
    "rollNo": 126016,
    "course": "Web Development",
    "semester": 3,
    "year": 2024,
    "email": "afzaalm993@gmail.com",
    "phone": "0300-1234567",
    "address": "House # 10, Street # 1, Nankana Sahib"
},
            {
    "userName":"Mian Haroon",
    "rollNo": 126017,
    "course": "Web Development",
    "semester": 3,
    "year": 2024,
    "email": "mianharoon@gmail.com",
    "phone": "0300-1234567",
    "address": "House # 12, Street # 3, Faisalabad"
},
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
# Write a programme that will return the data of the student whose Roll no is given by the user using path variable.

# Query Parameter 
# Receiving Data From Front-End to the Back-End through Query Parameter

@app.get("/getformdata")
def getRollNo(userName:str, rollNo:str):
    print("Student Name is", userName, "&", "Student Roll no is", rollNo)
    return "Students Addmissions form"


def start():
    uvicorn.run("students_crud.main:app",host="127.0.0.1", port=8181, reload=True)