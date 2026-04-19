import streamlit as st
import pandas as pd
import joblib
import os
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="HR Performance Dashboard", layout="wide")

# 1. Load Data & Model
@st.cache_data
def load_data():
    return pd.read_csv('data/employee_raw.csv')

def load_model():
    return joblib.load('models/perf_model.pkl')

# Sidebar for Navigation
st.sidebar.title("HR Control Panel")
page = st.sidebar.selectbox("Choose Page", ["Dashboard", "Individual Predictor"])

if page == "Dashboard":
    st.title("📊 Employee Performance Analytics Dashboard")
    df = load_data()

    # Top Metrics (KPIs)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Employees", len(df))
    col2.metric("High Performers", len(df[df['perf_rating'] == 'High']))
    col3.metric("Avg Evaluation Score", f"{df['last_eval_score'].mean():.2f}")

    # Charts Row
    st.markdown("---")
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Department-wise Employees")
        fig1 = px.bar(df['dept'].value_counts(), labels={'value':'Count', 'index':'Dept'}, color=df['dept'].value_counts().index)
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        st.subheader("Performance Breakdown")
        fig2 = px.pie(df, names='perf_rating', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig2, use_container_width=True)

    # Data Table
    st.subheader("Recent Employee Records")
    st.dataframe(df.head(10), use_container_width=True)

else:
    st.title("🔍 Predict Individual Employee Performance")
    model = load_model()

    # Form for User Input
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            dept = st.selectbox("Department", ['Tech', 'Sales', 'HR', 'Fin', 'Ops'])
            projects = st.number_input("Projects Completed", 1, 20, 5)
            hours = st.slider("Monthly Working Hours", 100, 300, 180)
        with col2:
            eval_score = st.slider("Last Evaluation Score", 0.0, 1.0, 0.7)
            satisfaction = st.slider("Satisfaction Level", 0.0, 1.0, 0.6)
            tenure = st.number_input("Tenure (Years)", 1, 15, 3)
            promo = st.radio("Promoted in last 5 years?", [0, 1])

        submit = st.form_submit_button("Predict Performance")

    if submit:
        # User input ko DataFrame mein convert karna
        input_data = pd.DataFrame([[dept, projects, hours, eval_score, tenure, satisfaction, promo]], 
                                 columns=['dept', 'projects', 'avg_hrs_month', 'last_eval_score', 'tenure_years', 'satisfaction', 'promotion_5yr'])
        
        prediction = model.predict(input_data)[0]
        
        # Result Show karna
        if prediction == 'High':
            st.success(f"### Predicted Performance: {prediction} 🌟")
        elif prediction == 'Medium':
            st.warning(f"### Predicted Performance: {prediction} ⚡")
        else:
            st.error(f"### Predicted Performance: {prediction} ⚠️")