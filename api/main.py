from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/ping")
async def hello():
    return "Hello, I am alive"

if __name__ == "__main__":
    uvicorn.run(app=app, host='localhost', port=8000)
