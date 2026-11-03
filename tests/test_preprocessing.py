import pandas as pd
from credit_risk.preprocessing import clean_data, split_features_target


def test_clean_data_removes_missing_rows():
    data = pd.DataFrame({"income": [1000, None], "default": [0, 1]})
    result = clean_data(data)
    assert len(result) == 1


def test_split_features_target():
    data = pd.DataFrame(
        {"income": [1000, 2000], "loan_amount": [300, 500], "default": [0, 1]}
    )
    X, y = split_features_target(data)
    assert list(X.columns) == ["income", "loan_amount"]
    assert list(y) == [0, 1]
