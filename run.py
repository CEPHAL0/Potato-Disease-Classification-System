import uvicorn
from api import app

uvicorn.run(app=app, host='localhost', port=8000, reload=True)
