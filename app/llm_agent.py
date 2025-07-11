import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_ndvi(ndvi_value):
    prompt = f"""
    The NDVI value from satellite imagery over Tel Aviv is {ndvi_value}.
    Explain what this means about the vegetation and land condition.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
