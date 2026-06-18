#Create a string variable with type hint.
name:str ="Yuvraj"
print(type(name))

#Create student_info() with hints.
def student_info(name: str, age: int, grade: float) -> str:
    return f"Name: {name}, Age: {age}, Grade: {grade}"


print(student_info("Yuvraj", 18, 92.5))


# Mini Project
# Student Profile System

name: str = "Yuvraj"
age: int = 19
cgpa: float = 8.5


def create_student(
    name: str,
    age: int,
    cgpa: float
) -> str:
    return f"Name: {name}\nAge: {age}\nCGPA: {cgpa}"


print(create_student(name, age, cgpa))
