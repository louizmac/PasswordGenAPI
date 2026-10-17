from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from core.generator import generate_password

app = FastAPI(
    title="PasswordGenAPI",
    description="A lightweight, open-source secure password generation REST API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://trymyapis.rf.gd"
    ],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return{
        "name": "PasswordGenAPI",
        "version": "1.0.0",
        "status": "online",
        "endpoints": [
            "/api/v1/password/generate"
        ]
    }

@app.get("/api/v1/password/generate")
def generate(
    length: int = Query(20, ge=8, le=128),
    uppercase: bool = True,
    lowercase: bool = True,
    numbers: bool = True,
    symbols: bool = True
):
    try:
        password = generate_password(
            length=length,
            uppercase=uppercase,
            lowercase=lowercase,
            numbers=numbers,
            symbols=symbols
        )

        return {
            "password": password,
            "length": len(password),
            "options": {
                "uppercase": uppercase,
                "lowercase": lowercase,
                "numbers": numbers,
                "symbols": symbols
            }
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )