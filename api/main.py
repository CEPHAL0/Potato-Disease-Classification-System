import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os
from fastapi import FastAPI, Body, HTTPException, status, File, UploadFile
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
# from bson import ObjectId
# from typing import Optional, List
# import motor.motor_asyncio
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
# db = client.college

MODEL = tf.keras.models.load_model("../deep_learning/models/model_1")
MODEL2 = tf.keras.models.load_model("../deep_learning/models/model_2")
CLASS_NAMES = ["early_blight", "late_blight", "healthy"]

# SCRIPT: uvicorn main:app --host localhost --port 8000 --reload

app = FastAPI()


# Configure CORS
origins = [
    "http://localhost:3000",  # Add your React frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # You can restrict this to specific HTTP methods if needed
    allow_methods=["*"],
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)


@app.get("/ping")
async def hello():
    return "Hello, I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image_nparray = np.array(image)
    return image_nparray


@app.post("/predict/v1")
async def predict(file: UploadFile = File()):

    image = read_file_as_image(await file.read())
    # bytes = await file.read()

    # The model accepts the data in format [[]] format but we have the image in [] format, so we have to expand the dims in the numpy array of the image

    img_batch = np.expand_dims(image, 0)
    predictions = MODEL.predict(img_batch)

    return f"Predictions using Model 1: {predictions}"


@app.post("/predict/v2")
async def predict(file: UploadFile = File()):

    image = read_file_as_image(await file.read())
    # bytes = await file.read()

    # The model accepts the data in format [[]] format but we have the image in [] format, so we have to expand the dims in the numpy array of the image

    img_batch = np.expand_dims(image, 0)
    predictions = MODEL2.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    confidence = np.max(predictions[0])

    return {
        "class": predicted_class,
        "confidence": str(confidence)
    }


@app.post("/login/details")
async def login_details(request_data: dict):
    print("Received JSON data from frontend:", request_data)
    # You can return a response if needed
    return {"message": "Data received successfully"}

if __name__ == "__main__":
    uvicorn.run(app=app, host='localhost', port=8000, reload=True)
