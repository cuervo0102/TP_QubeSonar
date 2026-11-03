from pathlib import Path
from sklearn.model_selection import train_test_split

from credit_risk.data import load_data
from credit_risk.preprocessing import clean_data, split_features_target
from credit_risk.training import RandomForestTrainer
from credit_risk.evaluation import evaluate_model
from credit_risk.prediction import save_model

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "raw" / "credit.csv"
MODEL_PATH = ROOT / "models" / "credit_model.joblib"


def run():
    data = load_data(DATA_PATH)
    data = clean_data(data)
    features, target = split_features_target(data)

    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42,
        stratify=target,
    )

    trainer = RandomForestTrainer()
    model = trainer.train(X_train, y_train)

    results = evaluate_model(model, X_test, y_test)
    print(f"Test accuracy: {results['accuracy']:.3f}")
    print("Confusion matrix:", results["confusion_matrix"])
    print(results["classification_report"])

    save_model(model, MODEL_PATH)
    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    run()
