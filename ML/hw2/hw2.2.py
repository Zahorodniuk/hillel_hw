import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import joblib

data = pd.read_csv('kc_house_data.csv')
#
# print(data.info())
# print(data.describe())

columns_for_regression = ['sqft_living', 'bedrooms', 'bathrooms', 'floors', 'sqft_lot', 'grade']
data = data[columns_for_regression + ['price']].dropna()

X = data[columns_for_regression]
y = data['price']

scaler = StandardScaler()
x_scaled = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
mse = mean_squared_error(y_test, y_predict)
print(f"Mean square deviation: {mse}")


joblib.dump(model, 'hw2_2_model.pkl')
loaded_model = joblib.load('hw2_2_model.pkl')
print(loaded_model)