import numpy as np
array1 = np.random.randint(-100, 100, 10)

average = np.mean(array1)
median = np.median(array1)
std = np.std(array1)
#print(array1)
#print('average mean:', average, 'median:', median,'standard deviation:', std)

array2 = np.random.randint(-100, 100, [3,3])

f_row = array2[0, :]
l_column = array2[:,-1]
diagonal = np.diagonal(array2)

#print('2D масив NumPy розміром (3, 3):\n', array2)
#print('first row:', f_row, 'last column:', l_column, 'diagonal:', diagonal)

array3_2d = np.random.randint(-100, 100, [3,3])
array3_1d = np.random.randint(-100, 100, [3])

sum_array = array3_2d + array3_1d

# print('2D масив NumPy розміром (3, 3):\n', array3_2d)
# print('1D масив розміром (3,):\n', array3_1d)
# print('Сума 1D масиву та кожного рядка 2D масиву:\n', sum_array)


array4 = np.random.randint(-100, 100, [5,5])

unique_numbers = np.unique(array4)
certain_value = 33
right_rows = array4[np.sum(array4, axis=1) > certain_value]

# print('2D масив NumPy розміром (5, 5)\n', array4)
# print('Bсі унікальні елементи у масиві:\n', unique_numbers)
# print('Pядки, сума елементів у яких більша за 33:\n', right_rows)




array5_1d = np.arange(1,21)
array5_2d = array5_1d.reshape(4,5)

# print('1D масив:\n', array5_1d)
# print('Перетворений 1D масив у 2D масив розміром (4, 5):\n',array5_2d)