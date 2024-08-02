# Question
# You are given a dataset with numerical features and a binary target. Implement a logistic regression classifier using Python and evaluate its performance using cross-validation. The dataset is provided as a CSV file with columns feature1, feature2, ..., featureN, and target.

# Load the dataset from the CSV file.
# Preprocess the data: handle missing values, if any.
# Split the data into features (X) and target (y).
# Implement a logistic regression classifier using Scikit-learn.
# Perform 5-fold cross-validation to evaluate the model's performance.
# Print the average accuracy and standard deviation from the cross-validation results.

# SAMPLE:
# feature1,feature2,feature3,target
# 0.5,1.2,3.1,0
# 1.5,2.3,1.1,1
# 2.5,0.3,0.5,0
# 3.5,1.3,4.1,1

import pandas as pd
from sklearn import LogisticRegressor, StandardScaler, cross_val_score

df = pd.read_csv('path/file.csv')

y = df['target']
X = df.drop('target', axis=1)

# Preprocess - impute missing values
for col in X.columns:
    X[col].fillna(X[col].mean())

# Standardize x-values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegressor()

cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')

print(f'cv_scores: {cv_scores}')