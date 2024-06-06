from fastapi import FastAPI, HTTPException, Request
from src.models.predict_model import predict_model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Allow CORS for all origins with all methods and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


@app.post("/predict")
async def predict(data: dict):
    try:
        predictions = predict_model("models/model.pkl", data)
        return predictions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/model-prediction")
async def model_prediction(request: Request):
    try:
        data = await request.form()

        usia = data["usia"]
        status_pernikahan = data["status_pernikahan"]
        jumlah_anak = data["jumlah_anak"]
        pendapatan = data["pendapatan"]
        fasilitas = data.getlist("fasilitas[]")
        preferensi = data.getlist("preferensi[]")
        fasilitas = ", ".join(fasilitas)
        preferensi = ", ".join(preferensi)

        data_dict = {
            "Usia": usia,
            "Status Pernikahan": status_pernikahan,
            "Jumlah Anak": jumlah_anak,
            "Pendapatan/Bulan": pendapatan,
            "Fasilitas Yang Diinginkan": fasilitas,
            "Preferensi Lingkungan": preferensi,
        }

        predictions = predict_model("models/model.pkl", data_dict)
        return predictions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
