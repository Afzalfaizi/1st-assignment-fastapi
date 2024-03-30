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

@app.get("/students")
def getStudents():
    return students

@app.get("/students/{126016}")
def get_student(rollNo: int):
    for student in students:
        if student["Student_ID"] == rollNo:
            return student
    return {"message": "Student not found"}


@app.post("/addStudent")
def addStudent(userName:str, rollNo:str):
    students.append({"userName":userName, "rollNo":rollNo})
    return students
    
@app.get( "/student/{rollNo}") # Get the student by Roll No using (variable Path) variable path is a method of getting data from frontend to the backend.
def getStudentByRollNo(rollNo):
    print(" get student Roll No", rollNo)
    return rollNo

def start():
    uvicorn.run("students_crud.main:app",host="127.0.0.1", port=8181, reload=True)