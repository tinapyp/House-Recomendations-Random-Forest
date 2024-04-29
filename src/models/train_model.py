import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle


def train_model(df: pd.DataFrame, save_path: str = "models") -> RandomForestClassifier:
    """
    Train a Random Forest classifier on the given DataFrame, save the model and encoders.

    Args:
        df (pd.DataFrame): Input DataFrame containing features and labels.
        save_path (str): Path to save the trained model and encoders. Default is "models".

    Returns:
        RandomForestClassifier: Trained Random Forest classifier.
    """

    # Data Preprocessing
    ## Rename Column Name
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

    ## Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the trained model
    with open(save_path + "/model.pkl", "wb") as f:
        pickle.dump(model, f)

    # Save the encoders
    with open(save_path + "/status_pernikahan_encoder.pkl", "wb") as f:
        pickle.dump(status_pernikahan_encoder, f)

    with open(save_path + "/pendapatan_bulan_encoder.pkl", "wb") as f:
        pickle.dump(pendapatan_bulan_encoder, f)

    with open(save_path + "/usia_scaler.pkl", "wb") as f:
        pickle.dump(usia_scaler, f)

    return model
