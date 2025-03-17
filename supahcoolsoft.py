import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
#from kpis import approved_percentage, number_approved, total_applications, approved, provider_kpis
from read_data import read_data
#from charts import approved_by_area_bar

df = read_data()

def layout():
    st.markdown("# Executive dashboard")
    
    st.markdown("This is a simple dashboard about employee data based of supahcoolsoft.csv")


    #st.markdown("## KPIs in Sweden")

    # labels = ("total_applications", "number approved", "approved percentage")
    # cols = st.columns(3)
    # kpis = (total_applications, number_approved, approved_percentage)

    # for col, label, kpi in zip(cols, labels, kpis):
    #     with col: 
    #         st.metric(label=label, value=kpi)

    # 


    st.markdown("## Raw data")
    st.dataframe(df)



if __name__ == "__main__":
    layout()


#use matplotlib, plotly express and streamlit for graphs separately