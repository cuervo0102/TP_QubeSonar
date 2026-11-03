import pandas as pd


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Remove rows containing missing values."""
    return data.dropna().copy()


def split_features_target(data: pd.DataFrame, target_column: str = "default"):
    """Separate input features (X) from the target (y)."""
    if target_column not in data.columns:
        raise ValueError(f"Missing target column: {target_column}")
    features = data.drop(columns=[target_column])
    target = data[target_column]
    return features, target
