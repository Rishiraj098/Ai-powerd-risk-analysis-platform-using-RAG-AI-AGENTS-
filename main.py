from fastapi import FastAPI, UploadFile, File
from services.rag import process_query, ingest_document

app = FastAPI(title="Enterprise Risk Intelligence API")

@app.get("/")
def home():
    return {"status": "Backend running successfully"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    ingest_document(content)
    return {"message": "Document ingested successfully"}

@app.post("/query")
def query_risk(question: str):
    response = process_query(question)
    return {"result": response}
