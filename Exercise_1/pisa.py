import streamlit as st
from read_data import read_pisa_data
from charts import score_by_location, trend_chart
from kpis import total_locations, total_records, subject_categories, time_range, indicators_categories
df = read_pisa_data()

def layout():
    st.markdown("# Pisa performance scores dashboard")

    st.markdown("a simple Dashboard about pisa performance scores based of PISA Performance Scores by Country and Year. By Dennis Kao")

    st.markdown("## Basic stats")

    labels = ("number of records", "number of locations", " time period")
    cols = st.columns(3)
    kpis = (total_records, total_locations, time_range)
    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=kpi)
    
    st.metric(label="performance indicators", value=indicators_categories)        
    
    st.metric(label="subject categories", value=subject_categories)

    st.subheader("sample of dataset")

    st.dataframe(df.head())

    st.markdown("## average scores by location")
    
    score_by_location()

    st.title("PISA trend visualization")

    with st.sidebar:
        st.header("Filter")
        country = st.selectbox("Choose country", df["LOCATION"].unique())
        subjects = st.multiselect("Choose subject", options=df["SUBJECT"].unique(), default=list(df["SUBJECT"].unique()))
        indicators = st.multiselect("Choose subject", options=df["INDICATOR"].unique(), default=list(df["INDICATOR"].unique()))
        time_frame = st.slider("Select year range", int(df["TIME"].min()), int(df["TIME"].max()), (int(df["TIME"].min()), int(df["TIME"].max())))

    trend_chart(df, country, subjects, indicators, time_frame)

    st.markdown("## Raw data")

    st.dataframe(df)
# streamlit run Exercise_2/pisa.py
if __name__ == "__main__":
    layout()