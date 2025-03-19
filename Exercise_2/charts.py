from read_data import read_data
import duckdb
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly_express as px
import numpy as np


# bar chart showing number of employees accross departments
#streamlit plot
def counts_per_dep():

    df = read_data()

    df = duckdb.query("""
                    SELECT 
                    COALESCE(Department, 'Other') AS Department,
                    COUNT(*) AS Count
                    FROM df
                    GROUP BY COALESCE(Department, 'Other')
                    ORDER BY Count DESC
                    """).df()
    
    st.bar_chart(df, x = "Department", y = "Count",
                y_label="Employees",
                color="#181717",
                horizontal= True)

#matplotlib plot histogram of salary distribution
def salary_hist():

    df = read_data()

    df = duckdb.query("""
                        SELECT 
                        Salary_SEK as Salary
                        FROM df
    """).df()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df, x="Salary", bins=25, color="#ff00ff", edgecolor='black', ax=ax)
    ax.set_xlabel("Salary (SEK)")
    ax.set_ylabel("Employees")
    ax.set_title("Salary Distribution", fontdict={'fontsize':16})
    ax.grid(True, axis='y') # endast y linje i grid
    st.pyplot(fig)
 
#plotly express plots
def salaries_department():
    df=read_data()

    df=duckdb.query("""
                    SELECT
                    Salary_SEK as Salary,
                    COALESCE(Department, 'Other') AS Department,
                    FROM df
                    WHERE Department IS NOT NULL
                     """).df()
    

    
    fig = px.box(df, x="Department", y="Salary",
             title="Salaries per Department",
             hover_data="Salary") 
    fig.show()
             


