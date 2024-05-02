import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from src.features.build_features import preprocess_data


def train_model(
    X: pd.DataFrame, y: pd.DataFrame, save_path: str = "models"
) -> RandomForestClassifier:
    """
    Train a Random Forest classifier on the given features and labels, save the model and encoders.

    Args:
        X (pd.DataFrame): Input DataFrame containing preprocessed features.
        y (pd.DataFrame): DataFrame containing labels.
        save_path (str): Path to save the trained model and encoders. Default is "models".

    Returns:
        RandomForestClassifier: Trained Random Forest classifier.
    """

    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the trained model
    with open(save_path + "/model.pkl", "wb") as f:
        pickle.dump(model, f)

    # Evaluate Model
    column_predicted = {1: "Nama Perumahan", 2: "Jenis Rumah", 3: "Tipe Rumah"}

    y_pred = model.predict(X_test)

    # Compute accuracy for each output separately
    for i in range(y_test.shape[1]):
        accuracy = accuracy_score(y_test.iloc[:, i], y_pred[:, i])
        print(f"Accuracy for output {column_predicted[i+1]}: {accuracy:.2f}%")

    return model
