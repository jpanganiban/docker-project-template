import os

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", 80))
DEBUG = os.environ.get("DEBUG", "true").lower() == "true"
