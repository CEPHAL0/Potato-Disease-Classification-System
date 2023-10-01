import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os
from fastapi import FastAPI, Body, HTTPException, status, File, UploadFile, APIRouter
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr


from schemas.index import User
# from bson import ObjectId
# from typing import Optional, List
# import motor.motor_asyncio


disease = APIRouter()

MODEL = tf.keras.models.load_model("../deep_learning/models/model_1")
MODEL2 = tf.keras.models.load_model("../deep_learning/models/model_2")
CLASS_NAMES = ["early_blight", "late_blight", "healthy"]

# SCRIPT: uvicorn main:app --host localhost --port 8000 --reload


@disease.get("/ping")
async def hello():
    return "Hello, I am alive"


# HELPER FUNCTION TO CONVERT THE IMAGE TO NUMPY ARRAY
def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image_nparray = np.array(image)
    return image_nparray


@disease.post("/predict/v1")
async def predict(file: UploadFile = File()):

    image = read_file_as_image(await file.read())
    # bytes = await file.read()

    # The model accepts the data in format [[]] format but we have the image in [] format, so we have to expand the dims in the numpy array of the image

    img_batch = np.expand_dims(image, 0)
    predictions = MODEL.predict(img_batch)

    return f"Predictions using Model 1: {predictions}"


@disease.post("/predict/v2")
async def predict(file: UploadFile = File()):

    image = read_file_as_image(await file.read())

    # Resize the image to the desired shape (256x256x3)
    target_shape = (256, 256, 3)
    image = Image.fromarray(image)
    image = image.resize((target_shape[1], target_shape[0]))
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


# class User(BaseModel):
#     username: str
#     password: str


@disease.post("/login/details")
async def login_details(request_data: User):
    print("Received JSON data from frontend:", request_data)
    # You can return a response if needed
    return {"message": request_data}
