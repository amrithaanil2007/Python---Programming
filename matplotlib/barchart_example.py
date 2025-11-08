import matplotlib.pyplot as plt

categories = ["Math","Science","English","History","Geography"]
scores=[88,92,80,75,85]

plt.bar(categories, scores,color="black")
plt.xlabel("subjects")
plt.ylabel("scores")
plt.title("Exam score by subjects")

plt.grid()
plt.show()