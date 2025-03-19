from read_data import read_data
from charts import counts_per_dep
df = read_data()


# labels = ("total number of employees ", "average age", "average salary")
#     cols = st.columns(3)
#     kpis = (total_number, avg_age, avg_salary)


#print()
tot_staff_num = df.index.values.max()
avg_age = df["Age"].sum()/100
avg_salary = df["Salary_SEK"].sum()/100
print(tot_staff_num, avg_age, avg_salary)



# number_approved = len(approved)
# total_applications = len(df)
# approved_percentage = f"{number_approved / total_applications*100:.1f}%"

# print(number_approved)
# print(total_applications)
# print(approved_percentage)

# def provider_kpis(provider):
#     applied = df.query(f"`Utbildningsanordnare administrativ enhet` == '{provider}'")
#     applications = len(applied)
#     approved = len(applied.query("Beslut == 'Beviljad'"))
    
#     return applications, approved

# print(provider_kpis("TGA Utbildning AB"))