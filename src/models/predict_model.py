import pickle
import pandas as pd

# Load the saved encoders
with open("models/status_pernikahan_encoder.pkl", "rb") as f:
    status_pernikahan_encoder = pickle.load(f)

with open("models/pendapatan_bulan_encoder.pkl", "rb") as f:
    pendapatan_bulan_encoder = pickle.load(f)

with open("models/usia_scaler.pkl", "rb") as f:
    usia_scaler = pickle.load(f)

unique_fasilitas = [
    "CCTV 24 Jam & Security",
    "Garden Lounge",
    "Jalan Menggunakan Paving Block",
    "Jalan Utama Yang Lebar",
    "Masjid",
    "One Gate System",
    "Smart Door Lock",
    "Smart Home System",
    "TK",
    "Taman Bermain Anak",
]

unique_lingkungan = [
    "Dekat Dengan ATM Center",
    "Dekat Dengan Exit Tol",
    "Dekat Dengan Pusat Kota",
    "Dekat Dengan Sarana Kesehatan",
    "Dekat Dengan Sarana Pendidikan",
    "Dekat Dengan Sarana Perbelanjaan",
    "Dekat Dengan Tempat Ibadah",
    "Dekat Dengan Tempat Kuliner",
    "Dekat Dengan Tempat Wisata",
    "Dilalui Dengan Kendaraan Umum",
    "Dilalui Dengan SPBU",
    "Suasana Sejuk Dan Asri",
    "View Pegunungan",
]


def predict_model(model_path: str, data_to_predict):
    # Load the model
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Convert data to a DataFrame with a single row
    data_df = pd.DataFrame(data_to_predict, index=[0])

    # Transform categorical variables
    status_pernikahan_encoded = status_pernikahan_encoder.transform(
        data_df["Status Pernikahan"]
    )
    pendapatan_bulan_encoded = pendapatan_bulan_encoder.transform(
        data_df["Pendapatan/Bulan"]
    )

    # Scale numerical feature "Usia"
    usia_scaled = usia_scaler.transform([data_df["Usia"]])[0][0]

    # Create one-hot encoded features for 'Fasilitas Yang Diinginkan'
    for split_elements in data_df["Fasilitas Yang Diinginkan"].str.split(", "):
        fasilitas_encoding = [
            1 if element in split_elements else 0 for element in unique_fasilitas
        ]

    # Create one-hot encoded features for 'Preferensi Lingkungan'
    for split_elements in data_df["Preferensi Lingkungan"].str.split(", "):
        lingkungan_encoding = [
            1 if element in split_elements else 0 for element in unique_lingkungan
        ]

    # Convert transformed data back to the expected format
    transformed_data = {
        "Usia": usia_scaled,
        "Status Pernikahan": status_pernikahan_encoded,
        "Jumlah Anak": data_df["Jumlah Anak"],
        "Pendapatan/Bulan": pendapatan_bulan_encoded,
        **{
            facility: encoding
            for facility, encoding in zip(unique_fasilitas, fasilitas_encoding)
        },
        **{
            lingkungan: encoding
            for lingkungan, encoding in zip(unique_lingkungan, lingkungan_encoding)
        },
    }

    # print(transformed_data)

    X_input = pd.DataFrame(transformed_data)
    y_pred = model.predict(X_input)

    y_pred = y_pred.tolist()
    if y_pred[0][0] == "Qianna Residence 2":
        y_pred[0][1] = "Komersil"
        y_pred[0][2] = "30/60"
    elif y_pred[0][0] == "Setiabudi Estate":
        y_pred[0][1] = "Komersil"
        y_pred[0][2] = "36/72"
    elif y_pred[0][0] == "Goalpara Hills":
        y_pred[0][1] = "Subsidi"
        y_pred[0][2] = "30/60"
    elif y_pred[0][0] == "Bukit Cibadak Asri":
        y_pred[0][1] = "Subsidi"
        y_pred[0][2] = "30/60"
    elif y_pred[0][0] == "Bukit Pinus Banjaran":
        y_pred[0][1] = "Subsidi"
        y_pred[0][2] = "30/60"

    prediction = {
        "namaPerumahan": y_pred[0][0],
        "jenisRumah": y_pred[0][1],
        "tipeRumah": y_pred[0][2],
    }
    return prediction
