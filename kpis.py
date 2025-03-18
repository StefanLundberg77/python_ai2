from read_data import read_data

df = read_data()


# labels = ("total number of employees ", "average age", "average salary")
#     cols = st.columns(3)
#     kpis = (total_number, avg_age, avg_salary)


#print()
roster = df.index.values.max()+1
avg_age = df["Age"].sum()/100
avg_salary = df["Salary_SEK"].sum()/100
print(roster, avg_age, avg_salary)


# total_number = roster
# average_age = 
# print(roster)
# approved = df.query("Beslut == 'Beviljad'")
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