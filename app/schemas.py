from pydantic import BaseModel

class CleanTextRequest(BaseModel):
    text: str

class CleanTextResponse(BaseModel):
        cleaned_text:str