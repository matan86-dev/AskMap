# AskMap - Satellite Imagery + GPT NDVI Summary

A minimal POC to analyze satellite images and describe the vegetation level using GPT-3.5.

## How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API
Visit: [http://localhost:8000/analyze](http://localhost:8000/analyze)

## Testing
```bash
pytest app/test_app.py
```

## Note
Add your `.tif` satellite image to the `data/` folder.
