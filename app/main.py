from fastapi import FastAPI
from app.image_processing import compute_ndvi
from app.llm_agent import summarize_ndvi

app = FastAPI()

@app.get("/analyze")
def analyze():
    image_path = "data/tel_aviv_sample.tif"
    ndvi = compute_ndvi(image_path)
    summary = summarize_ndvi(ndvi)
    return {"ndvi": ndvi, "summary": summary}
