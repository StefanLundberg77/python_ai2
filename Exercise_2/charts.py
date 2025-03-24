from read_data import read_data, read_pisa_data
import duckdb
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px



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
    sns.histplot(df, x="Salary", bins=25, color="violet", edgecolor='black', ax=ax,)
    ax.set_xlabel("Salary (SEK)")
    ax.set_ylabel("Employees")
    ax.set_title("Salary Distribution", fontdict={'fontsize':16})
    #ax.grid(True, axis='y') # endast y linje i grid
    st.pyplot(fig)
 
#plotly express plots boxplot
def salaries_department():
    df=read_data()

    df=duckdb.query("""
                    SELECT
                    Salary_SEK as Salary,
                    COALESCE(Department, 'Other') AS Department,
                    FROM df

                     """).df()

    fig = px.box(df, x="Department", y="Salary", 
             title="Salaries per Department",
             hover_data="Salary", color_discrete_sequence=['black']) 
    st.plotly_chart(fig)
             
#histogram of age distribution
def age_hist():

    df = read_data()

    df = duckdb.query("""
                    SELECT 
                    Age,
                    FROM df
                    """).df()

    fig = px.histogram(df, x = "Age", title="Age distribution",nbins=100, text_auto=True, color_discrete_sequence=['brown'])
    
    st.plotly_chart(fig)

    # box plot of ages by department

def age_by_dep():

    df = read_data()

    df = duckdb.query("""
                    SELECT 
                    Age,
                    COALESCE(Department, 'Other') AS Dep
                    FROM df
                    """).df()
        
    fig, ax = plt.subplots(figsize=(10,6))
    sns.boxplot(df, x="Dep", y="Age", color="brown", ax=ax)
    ax.set_xlabel("Department")
    ax.set_ylabel("Age")
    ax.set_title("Age distribution by department")
    st.pyplot(fig)

    # pisa charts
    # bar chart showing average PISA scores by location

def score_by_location():
    df = read_pisa_data()

    df = duckdb.query("""SELECT
                        AVG(Value) as Value, 
                        LOCATION
                        FROM df
                        GROUP BY LOCATION 
                        ORDER BY Value """).df()
    
    import plotly.express as px

    fig = px.bar(df, x='LOCATION', y='Value', 
                title='Average PISA Score by Location', 
                color_discrete_sequence=['darkgreen'])
    fig.update_layout(xaxis_tickangle=-45)
    fig.update_yaxes(range=[0, 600])
    st.plotly_chart(fig, use_container_width=True)

  
def trend_chart(df, country, subjects, indicators, time_frame):
    df = read_pisa_data()
    # Filtrera data baserat på alla val
    filtered_data = df[
        (df["LOCATION"] == country) &
        (df["SUBJECT"].isin(subjects)) &
        (df["INDICATOR"].isin(indicators)) &
        (df["TIME"] >= time_frame[0]) &
        (df["TIME"] <= time_frame[1])
    ]

    if filtered_data.empty:
        st.warning("No data matches the selected filters.")
        return


    fig = px.line(
        filtered_data, 
        x="TIME", 
        y="Value", 
        color="INDICATOR", 
        line_dash="SUBJECT", 
        markers=True, 
        title=f"PISA trends for {country}",
        hover_data=["SUBJECT", "TIME", "Value"]
    )

    fig.update_layout(width=800, height=500)
    st.plotly_chart(fig, use_container_width=True)