import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama-3.3-70b-versatile"   # ← updated
MAX_TOKENS = 300
DEFAULT_ROUNDS = 3
TRANSCRIPTS_DIR = "transcripts"