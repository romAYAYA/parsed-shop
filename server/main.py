import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import register_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
)

app.include_router(register_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8800, reload=True)
