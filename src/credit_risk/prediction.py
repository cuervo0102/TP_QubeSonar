from pathlib import Path
import joblib
import pandas as pd


def save_model(model, path: str | Path) -> None:
    """Save a trained model to disk."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


def load_model(path: str | Path):
    """Load a previously saved model."""
    return joblib.load(path)


def predict(model, customer_data: pd.DataFrame):
    """Predict default (1) or no default (0) for customer rows."""
    return model.predict(customer_data)
