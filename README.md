
---

# 🚀 EMPLOYEE PERFORMANCE PREDICTOR

### 📌 **PROJECT OVERVIEW**

* **Goal:** Developing a data-driven system to analyze and predict employee performance levels.
* **Problem:** Manual performance reviews are often biased or delayed, making it hard for HR to identify top talent or at-risk employees.
* **Solution:** Using **Machine Learning** to evaluate key parameters and provide an objective performance score for each employee.

---

### 💼 **BUSINESS VALUE (HR ANALYTICS)**

* **Identify High Performers:** Helps in making fair and data-backed promotion decisions.
* **Proactive Training:** Detects employees with low performance early so they can be provided with necessary training.
* **Retention Strategy:** Identifies patterns that lead to high productivity, helping HR improve the overall work environment.

---

### 🛠️ **CORE FEATURES**

* **Predictive Modeling:** Uses **Classification Algorithms** to categorize performance (e.g., Low, Medium, High).
* **Feature Importance:** Identifies which factors (like training, years of experience, or last rating) impact performance the most.
* **Data Visualization:** Built-in charts to show department-wise performance trends.
* **Interactive UI:** A **Streamlit Dashboard** where HR can input employee details and get instant predictions.

---

### 📂 **PROJECT STRUCTURE**

* `data/` — Contains employee datasets (Synthetic/Public).
* `models/` — Saved trained models (`.pkl` files) for quick deployment.
* `src/` — Python scripts for Data Cleaning, EDA, and Model Training.
* `app/` — Streamlit web app files for the final user interface.
* `reports/` — Visual analysis of employee distribution and performance metrics.

---

### 🚀 **HOW TO RUN THIS PROJECT**

**1. Clone the repository**

```bash
git clone https://github.com/dakshh-23/employee-performance-predictor.git
cd employee-performance-predictor

```

**2. Install dependencies**

```bash
pip install -r requirements.txt

```

**3. Run the Training script**

```bash
python src/train_model.py

```

**4. Start the Dashboard**

```bash
streamlit run app/main.py

```

---

### 📊 **EVALUATION METRICS**

* **Accuracy & Precision:** Measures how correctly the model predicts each performance category.
* **Recall:** Crucial for identifying low performers so that no employee who needs help is missed.

---

### 👤 **AUTHOR**

* **Dakshata Patil**
* **Role:** Data Scientist / HR Analytics Specialist
* **GitHub:** [@dakshh-23](https://www.google.com/search?q=https://github.com/dakshh-23)

---

