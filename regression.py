import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

diabetes = load_diabetes()

diabetes_df = pd.DataFrame(data=np.c_[diabetes.data, diabetes.target], columns=diabetes.feature_names + ['target'])

model = LinearRegression()
model.fit(diabetes.data, diabetes.target)

original_accuracy = model.score(diabetes.data, diabetes.target)
print(f'Original R^2 Score: {original_accuracy:.4f}')

feature_importances_score = {}

for feature in diabetes.feature_names:
    temp_df = diabetes_df.drop(feature, axis=1)

    X = temp_df.drop('target', axis=1)
    y = temp_df['target']
    model.fit(X, y)
    score = model.score(X, y)
    feature_importances_score[feature] = score


sorted_feature_importances_score = sorted(feature_importances_score.items(), key=lambda x: x[1], reverse=True)

top_3_positive_features_score = sorted_feature_importances_score[:3]

print("\nTop 3 Positive Impact Features (Score):")
for feature, score in top_3_positive_features_score:
    print(f'{feature}: {score:.4f}')

feature_importances_rmse = {}

for feature in diabetes.feature_names:
    temp_df = diabetes_df.drop(feature, axis=1)

    X = temp_df.drop('target', axis=1)
    y = temp_df['target']
    model.fit(X, y)
    y_pred = model.predict(X)
    rmse = sqrt(mean_squared_error(y, y_pred))
    feature_importances_rmse[feature] = rmse


sorted_feature_importances_rmse = sorted(feature_importances_rmse.items(), key=lambda x: x[1])

top_3_lowest_rmse_features = sorted_feature_importances_rmse[:3]



print("\nTop 3 Features with Lowest RMSE:")
for feature, rmse in top_3_lowest_rmse_features:
    print(f'{feature}: {rmse:.4f}')
