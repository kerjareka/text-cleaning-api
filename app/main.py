from fastapi import FastAPI
from app.preprocessing import clean_text
from app.schemas import CleanTextRequest, CleanTextResponse

app = FastAPI(
    title="Indonesian Text Cleaning API",
    description="API for preprocessing Indonesian text for NLP tasks",
    version="1.0.0"
)

@app.post("/clean-text", response_model=CleanTextResponse)
def clean_text_endpoint(request: CleanTextRequest):
    result = clean_text(request.text)
    return {"cleaned_text": result}