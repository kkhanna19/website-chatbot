import os
from dotenv import load_dotenv

load_dotenv()

# AWS Bedrock Config
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

LLM_MODEL = os.getenv("LLM_MODEL", "mistral.mistral-large-3-675b-instruct")