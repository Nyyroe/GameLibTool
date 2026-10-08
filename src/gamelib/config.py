import os
from pathlib import Path
from dotenv import load_dotenv

# figure out the root from the file location
FILE_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(FILE_ROOT/".env")
STEAM_API_KEY = os.getenv("STEAM_API_KEY")

if not STEAM_API_KEY:
    raise RuntimeError(f"The Steam key is missing or empty. Please ensure a .env file exists which matches the .env example. Otherwise check that the .env file is located in {FILE_ROOT}")

RAW_DIR = FILE_ROOT / "data" / "raw"
PROCESSED_DIR = FILE_ROOT / "data" / "processed"
