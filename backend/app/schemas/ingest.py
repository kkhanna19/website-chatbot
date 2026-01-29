from pydantic import BaseModel, HttpUrl

class IngestRequest(BaseModel):
    url: HttpUrl

class IngestResponse(BaseModel):
    status: str
    chunks: int
