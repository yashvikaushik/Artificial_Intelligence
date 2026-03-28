from pydantic import BaseModel,Field,EmailStr
from typing import Optional

class Student(BaseModel):
    name: str='yashvi kaushik'
    age: Optional[int]=None
    cgpa:float=Field(gt=0,lt=10,default=7.5,description="your cgpa please")
    email:EmailStr



student=Student(name='rishi',age='32',email='yashvikaushik2525@gmail.com')
print(student)