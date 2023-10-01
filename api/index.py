from fastapi import FastAPI
from routes.index import user, disease
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # React frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # You can restrict this to specific HTTP methods if needed
    allow_methods=["*"],
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)

app.include_router(user, prefix="/user")
app.include_router(disease, prefix="/disease")
