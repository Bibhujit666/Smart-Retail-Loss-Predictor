import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import joblib

# ✅ Load dataset
df = pd.read_csv("../data/retail_data.csv")

print("📊 Columns:", df.columns)

# ✅ Drop missing values
df = df.dropna()

# ============================
# 🎯 FEATURES
# ============================
X = df[[
    "temperature_c",
    "humidity_percent",
    "footfall",
    "active_staff_on_shift",
    "avg_staff_experience_years",
    "cold_chain_break_minutes",
    "is_weekend"
]]

# ============================
# 🔥 REGRESSION MODEL
# ============================
y_reg = df["shrinkage_value_inr"]   # OR spoilage_value_inr

X_train, X_test, y_train, y_test = train_test_split(
    X, y_reg, test_size=0.2, random_state=42
)

reg_model = RandomForestRegressor(n_estimators=100, random_state=42)
reg_model.fit(X_train, y_train)

reg_score = reg_model.score(X_test, y_test)
print(f"✅ Regression R2 Score: {reg_score}")

# ============================
# 🚨 CLASSIFICATION MODEL
# ============================
y_clf = df["high_shrinkage_risk"]   # OR high_spoilage_risk

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X, y_clf, test_size=0.2, random_state=42
)

clf_model = RandomForestClassifier(n_estimators=100, random_state=42)
clf_model.fit(X_train_c, y_train_c)

clf_score = clf_model.score(X_test_c, y_test_c)
print(f"✅ Classification Accuracy: {clf_score}")

# ============================
# 🧠 FEATURE IMPORTANCE
# ============================
importance = pd.Series(reg_model.feature_importances_, index=X.columns)
print("\n🔥 Top Features:")
print(importance.sort_values(ascending=False))

# ============================
# 💾 SAVE MODELS
# ============================
joblib.dump(reg_model, "regressor.pkl")
joblib.dump(clf_model, "classifier.pkl")

print("\n✅ Models saved:")
print("📦 regressor.pkl (loss prediction)")
print("📦 classifier.pkl (risk prediction)")