import numpy as np

marks = np.array([45, 82, 91, 67, 78, 85, 59])

print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Marks greater than 80:", marks[marks > 80])