import matplotlib.pyplot as plt

departments = ["IT","Finance","HR"]
salaries = [60000,7000,50000]

plt.bar(departments , salaries ,  color = ["blue","green","orange"],width=0.5)
plt.title("Average salaries by department")
plt.xlabel("DEpartments")
plt.ylabel("Average salaries")

plt.show()

plt.barh(departments , salaries ,  color = ["lavender"],width=0.5)
plt.title("Average salaries by department")
plt.xlabel("DEpartments")
plt.ylabel("Average salaries")

plt.show()