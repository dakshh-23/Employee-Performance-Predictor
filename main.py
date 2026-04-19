from src.data_gen import DataGenerator  # Yaha ab error nahi aayegi
from src.preprocess import get_preprocessor
from src.model_trainer import ModelTrainer
import pandas as pd
from sklearn.model_selection import train_test_split

def start_pipeline():
    # 1. Generate Data
    gen = DataGenerator()
    gen.run(n=2000)

    # 2. Load and Split
    df = pd.read_csv('data/employee_raw.csv')
    X = df.drop(['emp_id', 'perf_rating'], axis=1)
    y = df['perf_rating']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Preprocess & Train
    preprocessor = get_preprocessor()
    trainer = ModelTrainer(preprocessor)
    trainer.train(X_train, y_train)

    # 4. Evaluation & Save
    trainer.evaluate(X_test, y_test)
    trainer.save()

if __name__ == "__main__":
    start_pipeline()