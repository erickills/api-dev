from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

# PATH OPERATION OR SOMETIMES REFER AS ROUTE 
# "@" -start of a decorator
# "/" - a root path PATH
#  "get" - method
#  root() - is the function,u can name it anything

@app.get("/") 
def root():   # FUNCTION Arbritrary name, you can name it anything. ex. login_user
    return {"message": "Welcome to my API!"}

@app.get("/posts") # PATH
def get_posts():
    return {"data": "this is a post test"}

@app.get("/about")
def about():
    return {"message": "This is a test for about"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return{"message": "Successfully created posts!!!"}


