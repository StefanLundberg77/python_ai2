from read_data import read_data

df = read_data()

#calculate kpis
total_staff_number = len(df)
salary = df["Salary_SEK"]
avg_age = df["Age"].sum()/total_staff_number
avg_salary = salary.sum()/total_staff_number
print(total_staff_number, avg_age, avg_salary)



# def provider_kpis(provider):
#     applied = df.query(f"`Utbildningsanordnare administrativ enhet` == '{provider}'")
#     applications = len(applied)
#     approved = len(applied.query("Beslut == 'Beviljad'"))
    
#     return applications, approved

# print(provider_kpis("TGA Utbildning AB"))