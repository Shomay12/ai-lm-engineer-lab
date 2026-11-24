
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL")

if not api_key or not model:
    raise ValueError("Set GROQ_API_KEY and OPENAI_MODEL in .env")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    model=model,
    input="Explain the difference between LLM training and inference in 3 sentences.",
    max_output_tokens=150,
    temperature=0.2,
    top_p=0.9,
)

print("MODEL:", model)

print("\nRESPONSE:")
print(response.output_text)

if response.usage:
    print("\nUSAGE:")
    print("Input tokens:", response.usage.input_tokens)
    print("Output tokens:", response.usage.output_tokens)
    print("Total tokens:", response.usage.total_tokens)
