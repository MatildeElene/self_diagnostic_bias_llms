# main.py
import os
import json
import time
import re

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

from config import MODELS


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found.")

client = OpenAI(api_key=api_key)

MODEL_CFG = MODELS["mini"]  # "mini" for development, "prod" for final