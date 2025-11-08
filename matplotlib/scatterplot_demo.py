import matplotlib.pyplot as plt

#sample data
x_values = [22,25,27,29,31,33,36]
y_values = [80,85,90,75,65,70,95]

plt.scatter(x_values ,y_values,color = "red",s = 100)
plt.xlabel("Age in Years")
plt.ylabel("weight in kilograms")
plt.title("Age versus Weight scatter plot")
plt.show()