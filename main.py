from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Petlove Sales Assistant API is running!"}

