"""
### Assignment 3: Object State Persistence with Pickle
#### Scenario
A machine learning experiment tracker records trained model hyperparameters and validation metrics. Researchers need to serialize experiment sessions to disk and reload them seamlessly.

#### Problem Description
1. Create a class `ExperimentSnapshot` with:
   - Attributes: `experiment_id` (str), `model_type` (str), `hyperparameters` (dict), `metrics` (dict), `timestamp` (str).
   - Method `get_best_metric(metric_name)`: Returns the numeric score for `metric_name` from `metrics`.
2. Create two helper functions:
   - `save_experiment(snapshot, file_path)`: Serializes the `ExperimentSnapshot` object to `file_path` in binary mode using `pickle.dump()`.
   - `load_experiment(file_path)`: Deserializes and returns the `ExperimentSnapshot` instance from `file_path`. If the file does not exist, raises `FileNotFoundError`.

#### Example Walkthrough
```python
exp = ExperimentSnapshot(
    experiment_id="EXP-2026-001",
    model_type="RandomForest",
    hyperparameters={"n_estimators": 100, "max_depth": 10},
    metrics={"accuracy": 0.942, "f1_score": 0.938},
    timestamp="2026-09-01 10:00:00"
)

save_experiment(exp, "experiment_01.pkl")

restored_exp = load_experiment("experiment_01.pkl")
print(restored_exp.model_type)                    # Output: RandomForest
print(restored_exp.get_best_metric("accuracy"))   # Output: 0.942
```
"""
import os
import pickle


class ExperimentSnapshot:
    def __init__(self, experiment_id: str, model_type: str, hyperparameters: dict, metrics: dict, timestamp: str):
        self.experiment_id = experiment_id
        self.model_type = model_type
        self.hyperparameters = hyperparameters
        self.metrics = metrics
        self.timestamp = timestamp

    def get_best_metric(self, metric_name: str):
        return self.metrics.get(metric_name)


def save_experiment(snapshot: ExperimentSnapshot, file_path: str):
    with open(file_path, "wb") as f:
        pickle.dump(snapshot, f)


def load_experiment(file_path: str) -> ExperimentSnapshot:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Experiment snapshot file '{file_path}' not found.")
    with open(file_path, "rb") as f:
        return pickle.load(f)


if __name__ == "__main__":
    pass
