from abc import ABC, abstractmethod
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


class ModelTrainer(ABC):
    """Common interface for all model trainers."""

    @abstractmethod
    def train(self, features, target):
        """Train and return a fitted model."""
        raise NotImplementedError


class RandomForestTrainer(ModelTrainer):
    def train(self, features, target):
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            class_weight="balanced",
        )
        model.fit(features, target)
        return model


class LogisticRegressionTrainer(ModelTrainer):
    def train(self, features, target):
        model = LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
        )
        model.fit(features, target)
        return model
