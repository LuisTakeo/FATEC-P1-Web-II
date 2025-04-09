from fastapi import FastAPI
import os
import uvicorn
from app import router, criar_db
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
app.include_router(router)
db_path = os.getenv("BD_NAME")
if not db_path:
    raise ValueError("BD_NAME não está definido no arquivo .env")
if not os.path.exists(db_path):
        criar_db()  

if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)
