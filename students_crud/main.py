from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
def getStudents():
    print(f"Getting all students...")
    return {"message": "Hello, this is a sample response for getting all the students."}
    
# Add a new student to the database
