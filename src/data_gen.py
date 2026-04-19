
import pandas as pd
import numpy as np
import os

class DataGenerator:
    def __init__(self, output_path='data/employee_raw.csv'):
        self.output_path = output_path

    def run(self, n=2000):
        print(f"Generating {n} smart employee records...")
        np.random.seed(42)
        
        projects = np.random.randint(2, 10, n)
        hours = np.random.randint(150, 250, n)
        evaluation = np.random.uniform(0.4, 1.0, n)
        satisfaction = np.random.uniform(0.3, 1.0, n)
        tenure = np.random.randint(1, 10, n)
        dept = np.random.choice(['Tech', 'Sales', 'HR', 'Fin', 'Ops'], n)
        promo = np.random.choice([0, 1], n, p=[0.9, 0.1])

        perf = []
        for i in range(n):
            if evaluation[i] > 0.8 and projects[i] > 6:
                perf.append('High')
            elif satisfaction[i] < 0.5 and hours[i] > 230:
                perf.append('Low')
            else:
                perf.append('Medium')

        df = pd.DataFrame({
            'emp_id': range(1001, 1001 + n),
            'dept': dept,
            'projects': projects,
            'avg_hrs_month': hours,
            'last_eval_score': evaluation,
            'tenure_years': tenure,
            'satisfaction': satisfaction,
            'promotion_5yr': promo,
            'perf_rating': perf
        })

        os.makedirs('data', exist_ok=True)
        df.to_csv(self.output_path, index=False)
        print(f"✅ Smart Data Generated at: {self.output_path}")

if __name__ == "__main__":
    gen = DataGenerator()
    gen.run()