# openai_client.py
import os

# LLM
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("OPENAI_API_KEY.env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# your config
from config import MODELS
MODEL_CFG = MODELS["mini"]   # use "mini" for dev; switch to "prod" for final

