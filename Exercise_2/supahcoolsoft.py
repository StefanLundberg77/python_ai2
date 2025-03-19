import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
from kpis import tot_staff_num, avg_age, avg_salary
from read_data import read_data
from charts import counts_per_dep

df = read_data()

def layout():
    st.markdown("# Executive dashboard")
    
    st.markdown("This is a simple dashboard about employee data based of supahcoolsoft.csv")

    st.markdown("## Basic statistics.")

    labels = ("total number of employees", "average age", "average salary")
    cols = st.columns(3)
    kpis = (tot_staff_num, avg_age, avg_salary)

    for col, label, kpi in zip(cols, labels, kpis):
        with col: 
            st.metric(label=label, value=kpi)
    
    counts_per_dep()

    st.markdown("## Raw data")

    st.dataframe(df)



if __name__ == "__main__":
    layout()


#use matplotlib, plotly express and streamlit for graphs separately