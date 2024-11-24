import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "4f3e4e8b9d1a2b4c5d6f7e8f9a0b1c2d3e4f5a6b7c8d9e0f")
    DEBUG = True  # Cambiar a False en producción
    OLLAMA_MODEL = "llama3.2-vision:11b"
