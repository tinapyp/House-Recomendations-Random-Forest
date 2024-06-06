import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the input DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame containing features.

    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    # Rename Column Names
    df = df.rename(
        columns={
            "Apakah ada fasilitas yang membuat Bapak/Ibu tertarik dengan rumah ini?": "Fasilitas Yang Diinginkan",
            "Apakah Bapak/Ibu memiliki preferensi tertentu terkait dengan lingkungan sekitar rumah?": "Preferensi lingkungan",
        }
    )

    ## Split into Input and Output
    X = df[
        [
            "Usia",
            "Status Pernikahan",
            "Jumlah Anak",
            "Pendapatan/Bulan",
            "Fasilitas Yang Diinginkan",
            "Preferensi lingkungan",
        ]
    ].copy()
    y = df[["Nama Perumahan", "Jenis Rumah", "Tipe Rumah"]].copy()

    ## Apply Label Encoding
    status_pernikahan_encoder = LabelEncoder()
    pendapatan_bulan_encoder = LabelEncoder()

    X["Status Pernikahan"] = status_pernikahan_encoder.fit_transform(
        X["Status Pernikahan"]
    )
    X["Pendapatan/Bulan"] = pendapatan_bulan_encoder.fit_transform(
        X["Pendapatan/Bulan"]
    )

    ## Make one Hot Encoding
    unique_fasilitas = set(
        [
            fasilitas
            for sublist in X["Fasilitas Yang Diinginkan"].str.split(", ")
            for fasilitas in sublist
        ]
    )
    for facility in unique_fasilitas:
        X[facility] = X["Fasilitas Yang Diinginkan"].str.contains(facility).astype(int)

    ## Remove Unnecessary Column
    X.drop("Fasilitas Yang Diinginkan", axis=1, inplace=True)

    ## Scale the age data
    usia_scaler = StandardScaler()
    X["Usia"] = usia_scaler.fit_transform(X[["Usia"]])

    return X, y
