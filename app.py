from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from src.models.predict_model import predict_model

app = FastAPI()


@app.post("/predict")
async def predict(request: Request):
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
        return predictions.tolist()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
