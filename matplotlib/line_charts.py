import matplotlib.pyplot as plt

days=["mon","tue","wed","thur","fri","sat","sun"]
visits = [250,270,300,280,350,400,420]

plt.plot(days,visits)
plt.title("Website Traffic Over a Week")
plt.xlabel("Days of the week")
plt.ylabel("Number of Visitors")
plt.show()

plt.plot(days,visits,color = "blue",linestyle="--",linewidth=2)
plt.title("Website Traffic Over a Week")
plt.xlabel("Days of the week")
plt.ylabel("Number of Visitors")
plt.show()

plt.plot(days,visits,color = "green",linestyle="--",linewidth="o")
plt.title("Website Traffic Over a Week")
plt.xlabel("Days of the week")
plt.ylabel("Number of Visitors")
plt.show()

visits_b = [200,230,250,220,300,320,330]
plt.plot(days,visits,label = "Website A",color="red",marker="o")
plt.plot(days,visits,label = "Website B",color="purple",marker="o")
plt.title("Website Traffic Over a Week")
plt.xlabel("Days of the week")
plt.ylabel("Number of Visitors")
plt.legend()
plt.show()