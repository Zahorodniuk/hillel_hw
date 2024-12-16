import pandas as pd

some_df = pd.DataFrame({
    'Ім\'я': ['Анна', 'Михайло', 'Наталія', 'Гліб', 'Світлана'],
    'Вік': [23, 15, 29, 41, 30],
    'Місто': ['Київ', 'Гайсин', 'Мукачево', 'Одеса', 'Вінниця']
})
some_df['Премія'] = [8500, 9000, 7300, 8080, 9054]

threshold = 8550
filtered_df = some_df[some_df['Премія'] > threshold]

print("Відфільтрований DataFrame:")
print(filtered_df)

data = pd.read_csv('wine.csv')

print("Перші 5 рядків датасету:")
print(data.head())

print("Загальна статистика для числових стовпців:")
print(data.describe())
