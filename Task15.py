import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

print(df)
print("Average salary:", df["salary"].mean())
print("Highest salary:", df["salary"].max())

plt.bar(df["name"], df["salary"])
plt.title("Employee Salaries")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.show()