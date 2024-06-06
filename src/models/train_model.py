import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)
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

    # Initialize lists to store metrics
    precisions = []
    recalls = []
    f1_scores = []

    # Compute confusion matrix and related metrics for each output separately
    for i in range(y_test.shape[1]):
        true_labels = y_test.iloc[:, i]
        predicted_labels = y_pred[:, i]

        # Compute confusion matrix
        conf_matrix = confusion_matrix(true_labels, predicted_labels)

        # Compute precision, recall, and F1-score
        precision = precision_score(true_labels, predicted_labels, average="weighted")
        recall = recall_score(true_labels, predicted_labels, average="weighted")
        f1 = f1_score(true_labels, predicted_labels, average="weighted")

        # Append metrics to respective lists
        precisions.append(precision)
        recalls.append(recall)
        f1_scores.append(f1)

        # Print the confusion matrix and related metrics for the ith output
        print(f"Confusion Matrix for output {i+1}:")
        print(conf_matrix)
        print(f"Precision for output {i+1}: {precision*100:.2f}%")
        print(f"Recall for output {i+1}: {recall*100:.2f}%")
        print(f"F1-score for output {i+1}: {f1*100:.2f}%")
        print()

    return model
