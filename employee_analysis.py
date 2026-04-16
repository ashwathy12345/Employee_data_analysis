import pandas as pd
import matplotlib.pyplot as plt

# Sample employee data
#data = {
#    "Name": ["John", "Alice", "Bob", "David", "Emma"],
#    "Department": ["IT", "HR", "IT", "Finance", "HR"],
#    "Salary": [50000, 40000, 60000, 55000, 45000],
#    "Experience": [2, 3, 5, 4, 2]
#}

#df = pd.DataFrame(data)
df = pd.read_csv("employee_data.csv")
print("\n--- Employee Data ---")
print(df)

# Average salary
avg_salary = df["Salary"].mean()
print("\nAverage Salary:", avg_salary)

# Highest salary
max_salary = df["Salary"].max()
print("Highest Salary:", max_salary)

# Department wise average salary
dept_salary = df.groupby("Department")["Salary"].mean()
print("\nDepartment-wise Average Salary:")
print(dept_salary)

# Filter employees with salary > 50000
high_salary = df[df["Salary"] > 50000]
print("\nEmployees with Salary > 50000:")
print(high_salary)



# Bar chart
dept_salary.plot(kind='bar')
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()