from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

MODEL = tf.keras.models.load_model("../deep_learning/models/model_1")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# SCRIPT: uvicorn main:app --host localhost --port 8000 --reload

app = FastAPI()


@app.get("/ping")
async def hello():
    return "Hello, I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image_nparray = np.array(image)
    return image_nparray


@app.post("/predict")
async def predict(file: UploadFile = File()):

    image = read_file_as_image(await file.read())
    # bytes = await file.read()

    # The model accepts the data in format [[]] format but we have the image in [] format, so we have to expand the dims in the numpy array of the image

    img_batch = np.expand_dims(image, 0)
    predictions = MODEL.predict(img_batch)

    return f"{predictions}"

if __name__ == "__main__":
    uvicorn.run(app=app, host='localhost', port=8000, reload=True)
