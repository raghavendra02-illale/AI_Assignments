
import pandas as pd

from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("student-mat.csv", sep=";")

# Input data
X = data[["studytime", "failures", "absences", "G1", "G2"]]

# Output data
y = (data["G3"] >= 10).astype(int)

# Create model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X, y)

# Give new student data
new_data = {
    "studytime": [3],
    "failures": [0],
    "absences": [2],
    "G1": [12],
    "G2": [15]
}

# Convert into DataFrame
new_df = pd.DataFrame(new_data)

# Predict result
prediction = model.predict(new_df)[0]

if prediction == 1:
    print("Student will Pass")
else:
    print("Student will Fail")
