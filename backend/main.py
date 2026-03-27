from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "app"))

from app.api.endpoints import router

app = FastAPI(
    title="Clawdbot API",
    description="Sistema de gestión contable para PYME",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir endpoints
app.include_router(router, prefix="/api")


# Endpoint raíz
@app.get("/")
def root():
    return {
        "mensaje": "🤖 Clawdbot API - Gestoría Virtual para PYME",
        "version": "1.0.0",
        "estado": "activo",
        "docs": "/docs",
    }


# Health check
@app.get("/health")
def health_check():
    return {"estado": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
