from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"msg":"This is the index , or the home page"}