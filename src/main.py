# main.py
import os, json, time, re
import pandas as pd

# LLM
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("OPENAI_API_KEY.env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# config
from config import MODELS
MODEL_CFG = MODELS["mini"]   # use "mini" for dev; switch to "prod" for final

