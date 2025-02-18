from fastapi import FastAPI, UploadFile, File, Form
from typing import List

# Create FastAPI app instance
app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI! 🚀"}

# File upload endpoint
@app.post("/v1/upload/")
async def upload_files(
    user_id: str = Form(...),
    department: str = Form(...),
    files: List[UploadFile] = File(...)
):
    # Store files in a variable
    file_data = []

    for file in files:
        file_contents = await file.read()  # Read file into memory (variable)

        file_data.append({
            "filename": file.filename,
            "content": file_contents,  # Binary content stored
            "size": len(file_contents)  # File size in bytes
        })

    return {
        "message": "File(s) received successfully! ✅",
        "user_id": user_id,
        "department": department,
        "files": [{"filename": f["filename"], "size": f["size"]} for f in file_data]
    }
