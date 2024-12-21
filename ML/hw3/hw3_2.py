import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Lasso, Ridge, ElasticNet
from sklearn.metrics import mean_squared_error

data = pd.read_csv('kc_house_data.csv')
data.head()

features = ['sqft_living', 'bedrooms', 'bathrooms', 'floors', 'sqft_lot', 'grade']
target = 'price'

X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

polym = PolynomialFeatures(degree=2, include_bias=False)
X_train_polym = polym.fit_transform(X_train_scaled)
X_test_polym = polym.transform(X_test_scaled)

X_train_polym.shape, X_test_polym.shape

models = {
    "Lasso": Lasso(alpha=1.0, random_state=42),
    "Ridge": Ridge(alpha=1.0),
    "ElasticNet": ElasticNet(alpha=1.0, l1_ratio=0.5, random_state=42)
}

results = {}
for name, model in models.items():
    model.fit(X_train_polym, y_train)
    y_pred = model.predict(X_test_polym)
    mse = mean_squared_error(y_test, y_pred)
    results[name] = mse

print(results)