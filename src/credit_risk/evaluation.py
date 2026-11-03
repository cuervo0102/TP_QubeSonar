from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def evaluate_model(model, features, target) -> dict:
    """Return common classification metrics."""
    predictions = model.predict(features)
    return {
        "accuracy": accuracy_score(target, predictions),
        "confusion_matrix": confusion_matrix(target, predictions).tolist(),
        "classification_report": classification_report(
            target, predictions, zero_division=0
        ),
    }
