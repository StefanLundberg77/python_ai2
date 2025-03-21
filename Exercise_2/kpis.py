from read_data import read_data, read_pisa_data
import duckdb
import streamlit as st
#supa data
df = read_data()

#calculate kpis for supah
total_staff_number = len(df)
salary = df["Salary_SEK"]
avg_age = df["Age"].sum()/total_staff_number
avg_salary = salary.sum()/total_staff_number
#print(total_staff_number, avg_age, avg_salary)

# pisa
df_pisa = read_pisa_data()

#calc kpis for pisa

#"number of records", "target locations", "number of test subjects", "time periods"
total_records = len(df_pisa)
total_locations = df_pisa['LOCATION'].nunique()
subjects = df_pisa['SUBJECT'].unique()
subject_categories = ", ".join(subjects)
time_range = f"{df_pisa['TIME'].min()} - {df_pisa['TIME'].max()}"
indicators = df_pisa['INDICATOR'].unique()
indicators_categories = ", ".join(indicators)

# test
print(subjects)