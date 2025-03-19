from read_data import read_data
import duckdb
import streamlit as st

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
                    ORDER BY Count DESC;
                    """).df()
    
    st.bar_chart(df, x = "Department", y = "Count")

#matplotlib plot

#plotly express plots


