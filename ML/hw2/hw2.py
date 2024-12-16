import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import joblib

data = pd.read_csv('kc_house_data.csv')

# print(data.info())
# print(data.describe())

plt.figure(figsize=(12, 8))
plt.scatter(data['sqft_living'], data['price'], alpha=0.3, marker='o', color='red')

plt.title("Залежність ціни від житлової площі")
plt.xlabel("Житлова площа (sqft_living)")
plt.ylabel("Ціна (price)")

plt.grid(alpha=0.5)

plt.savefig('sqft_price.png')
plt.show()


x = data[['sqft_living']]
y = data['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
mse = mean_squared_error(y_test, y_predict)
print(f"Mean square deviation: {mse}")


joblib.dump(model, 'hw2_1_model.pkl')
loaded_model = joblib.load('hw2_1_model.pkl')
print(loaded_model)
