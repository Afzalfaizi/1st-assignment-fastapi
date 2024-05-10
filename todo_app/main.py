from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, create_engine

# # ****************************************************************************************#
#  --------------------------------  Full Stack Todo App  ---------------------------------
# # ****************************************************************************************#

app = FastAPI()

connection_string = 'postgressql://postgres.aaukslgprmevbkiwnjvl:Ifltp3*789258@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres '
connection = create_engine(connection_string)


class students(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True) 
    name: str
    description: str
    is_completed: bool 

SQLModel.metadata.create_all(connection)






def start():
    uvicorn.run("students_crud.main:app",host="127.0.0.1", port=8080, reload=True)
    
    

# students = [{
#     "userName":"Muhammad Afzal",
#     "rollNo": 126016,
#     "course": "Web Development",
#     "semester": 3,
#     "year": 2024,
#     "email": "afzaalm993@gmail.com",
#     "phone": "0300-1234567",
#     "address": "House # 10, Street # 1, Nankana Sahib"
# },
#             {
#     "userName":"Mian Haroon",
#     "rollNo": 126017,
#     "course": "Web Development",
#     "semester": 3,
#     "year": 2024,
#     "email": "mianharoon@gmail.com",
#     "phone": "0300-1234567",
#     "address": "House # 12, Street # 3, Faisalabad"
# },
# ]

# @app.get("/")
# def getStudents():
#     return students


# # Path Variable 
# # Receiving Data From Front-End to the Back-End through Path Variable 
# @app.get("/getrollno/{rollNo}")
# def getRollNo(rollNo):
#     print("The Roll No of Muhammad Afzal (Student of Web Development) is", rollNo)
#     return rollNo 
# # Write a programme that will return the data of the student whose Roll no is given by the user using path variable.

# @app.get("/students/{rollNo}")
# def get_student(rollNo: int):
#     for student in students:
#         if student["rollNo"] == rollNo:
#             return student
#     return {"error": "Student not found"}

# @app.get("/addStudent") # Recieving Data from front-end to back-end through query Parameters.
# def addStudents(userName:str, rollNo:int, course:str, semester:int, year:int, email:str, phone:str, address:str):
#     global students
#     students.append({
#         "userName":userName,
#         "rollNo": rollNo,
#         "course": course,
#         "semester": semester,
#         "year": year,
#         "email": email,
#         "phone": phone,
#         "address": address
#     })
#     return students
# # Delete a students from object
# @app.delete("/deleteStudent/{rollNo}")
# def delete_student(rollNo: int):
#     global students
#     for i, student in enumerate(students):
#         if student["rollNo"] == rollNo:
#             del students[i]
#     return {"message": "Student deleted successfully"}
# # Query Parameter 
# # Receiving Data From Front-End to the Back-End through Query Parameter
# @app.get("/getformdata")
# def getRollNo(userName:str, rollNo:str):
#     print("Student Name is", userName, "&", "Student Roll no is", rollNo)
#     return "Student Data Add Successfully"
# # Pydantic 
# # Annotated
# # Request Body parameters (Secure way of receiving data) for security purposes.
#  # Pydantic Dict ki specific item ko different type deny k liye use krty hain.
#  # Annotated Data validation  k liye use krty hain. 
 
#  # Request Body Params
# class Item(BaseModel):
#     id:int
#     title:str
#     description:str

# @app.get("/student")
# def MainRoute(item:Item = None):
#     return item 