from fastapi import FastAPI, HTTPException
from typing import Dict, Any
from src.models.predict_model import predict_model

app = FastAPI()


@app.post("/predict")
async def predict(data: Dict[str, Any]):
    try:
        predictions = predict_model("models/model.pkl", data)
        return predictions.tolist()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
