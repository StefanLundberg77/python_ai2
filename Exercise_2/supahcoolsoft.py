import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
from kpis import total_staff_number, avg_age, avg_salary, salary
from read_data import read_data
from charts import counts_per_dep, salary_hist, salaries_department

df = read_data()

def layout():
    st.markdown("# Executive dashboard")
    
    st.markdown("This is a simple dashboard about employee data based of supahcoolsoft.csv")

    st.markdown("## Basic statistics.")

    labels = ("total number of employees", "average age", "average salary")
    cols = st.columns(3)
    kpis = (total_staff_number, avg_age, avg_salary)

    for col, label, kpi in zip(cols, labels, kpis):
        with col: 
            st.metric(label=label, value=kpi)
    
    counts_per_dep()

    salary_hist()

    salaries_department()

    st.markdown("## Raw data")

    st.dataframe(df)

# streamlit run Exercise_2/supahcoolsoft.py

if __name__ == "__main__":
    layout()


#use matplotlib, plotly express and streamlit for graphs separately