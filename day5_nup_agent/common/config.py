import os

from dotenv import load_dotenv

load_dotenv(override=True)

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL="gpt-5.4-mini"

BASE_URL = os.getenv("MODEL_BASE_URL")
FURIOSA_MODEL = os.getenv("MODEL_ID", "furiosa-ai/Qwen3-8B-FP8")

TEMPERATURE = os.getenv("LLM_TEMPERATURE", 2)
MAX_TOKENS = os.getenv("LLM_MAX_TOKENS", 2086)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "text-embedding-3-small"
)

# QDRANT_URL = os.getenv(
#     "QDRANT_URL",
#     "http://localhost:6333"
# )