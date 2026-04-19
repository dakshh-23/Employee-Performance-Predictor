from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import os

class ModelTrainer:
    def __init__(self, preprocessor):
        self.pipeline = Pipeline([
            ('pre', preprocessor),
            ('clf', RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42))
        ])

    def train(self, X_train, y_train):
        print("Training Random Forest Model...")
        self.pipeline.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        predictions = self.pipeline.predict(X_test)
        print("\n--- PERFORMANCE REPORT ---")
        print(classification_report(y_test, predictions))

    def save(self, path='models/perf_model.pkl'):
        os.makedirs('models', exist_ok=True)
        joblib.dump(self.pipeline, path)
        print(f"✅ Model saved to: {path}")