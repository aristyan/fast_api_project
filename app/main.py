from fastapi import FastAPI, File, UploadFile
import json
from app.features import feature_extraction


app = FastAPI()


''' Checking the health of the API returns only {status: "UP"} if the API is up and running. '''
@app.get("/")
def home():
    return {"status": "UP"}


''' Uploading the data in a JSON format and returning the results of the 'feature engineering' process in a JSON format '''
@app.post("/extract_features")
async def root(file: UploadFile = File(...)):
    try:
        json_data = json.load(file.file)
        features_extracted = feature_extraction(json_data)
        return {"features_extracted": features_extracted}
    except:
        return {"Error": "The File Format Is Invalid"}
