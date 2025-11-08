import matplotlib.pyplot as plt

x_values = [1,2,3,4,5,6,7,8]
y_values = [18,4,18,4,18,4,18,4]

plt.plot(x_values, y_values)

plt.xlabel("x Axis Values")
plt.ylabel("y Axis Values")
plt.title("My first matplotlib plot")

plt.plot(x_values, y_values,color="purple",marker="o")
plt.grid()
plt.show()