import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# STEP 1: Load dataset
data = pd.read_csv("usage_data.csv")

# STEP 2: Separate features and target
X = data[["Social", "Entertainment", "Productive", "Night", "Unlocks"]]
y = data["Risk"]

# STEP 3: Encode target labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# STEP 4: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42)

# STEP 5: Create model
model = RandomForestClassifier()

# STEP 6: Train model
model.fit(X_train, y_train)

# STEP 7: Check accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Training Completed")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# ===========================
# PREDICTION PHASE
# ===========================

print("\nEnter Today's Usage Data")

social = float(input("Social Media Hours: "))
entertainment = float(input("Entertainment Hours: "))
productive = float(input("Productive Hours: "))
night = float(input("Night Usage Hours: "))
unlocks = int(input("Number of Unlocks: "))

new_data = [[social, entertainment, productive, night, unlocks]]

prediction = model.predict(new_data)
risk_level = encoder.inverse_transform(prediction)

print("\nPredicted Addiction Risk:", risk_level[0])

# AI Recommendation System
if risk_level[0] == "High":
    print("\n⚠ High Addiction Risk Detected!")
    print("Recommendations:")
    print("- Activate Focus Mode for 2 hours")
    print("- Disable social notifications")
    print("- Avoid phone after 10 PM")
    
elif risk_level[0] == "Medium":
    print("\n⚠ Moderate Risk")
    print("Recommendations:")
    print("- Reduce social media by 1 hour")
    print("- Try 25-minute Pomodoro sessions")
    
else:
    print("\n✅ Healthy Digital Pattern")
    print("Keep maintaining this balance!")