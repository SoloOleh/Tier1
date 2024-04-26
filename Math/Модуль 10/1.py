import pandas as pd

# шлях до датасету з даними про будинки Мельбурну
melbourne_file_path = 'Math/Модуль 10/melb_data.csv'

# Створіть об'єкт, який міститиме в собі наш датасет
melbourne_data = pd.read_csv(melbourne_file_path)

melbourne_data.describe() #На виході отримуємо базові статистичні дані:

melbourne_data.head()



#count - кількість даних
#mean - середнє арифметичне
#std - стандартне відхилення
