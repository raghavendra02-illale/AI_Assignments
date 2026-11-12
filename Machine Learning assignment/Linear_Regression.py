
import pandas as pd

from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student-mat.csv", sep=";")

# Input data
X = data[["studytime", "failures", "absences", "G1", "G2"]]

# Output data
y = data["G3"]

# Create model
model = LinearRegression()

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

# Predict marks
predicted_marks = model.predict(new_df)[0]

print(f"Predicted Final Marks: {predicted_marks:.2f}")
