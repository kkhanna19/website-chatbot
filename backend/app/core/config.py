import os
from dotenv import load_dotenv

load_dotenv()

# AWS Bedrock Config
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# Model ID for Qwen on Bedrock (Check your AWS console for exact ID)
LLM_MODEL = os.getenv("LLM_MODEL", "qwen.qwen25-72b-instruct-v1:0")