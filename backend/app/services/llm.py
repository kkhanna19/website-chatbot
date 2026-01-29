import boto3
import json
from app.core.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION
from app.core.prompt import SYSTEM_PROMPT

# Initialize Bedrock Runtime client
client = boto3.client(
    service_name="bedrock-runtime",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

def generate_answer(context: str, question: str) -> str:
    model_id = "mistral.mistral-large-3-675b-instruct"
    
    # Modern Bedrock Converse API format
    messages = [
        {
            "role": "user",
            "content": [{"text": f"Context:\n{context}\n\nQuestion: {question}"}]
        }
    ]

    try:
        response = client.converse(
            modelId=model_id,
            messages=messages,
            system=[{"text": SYSTEM_PROMPT}],
            inferenceConfig={"maxTokens": 1024, "temperature": 0.2}
        )
        
        return response["output"]["message"]["content"][0]["text"]

    except Exception as e:
        return f"Bedrock Error: {str(e)}"