from datetime import datetime

def get_str_date(date):
    # Parse the date string to a datetime object
    date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')

    # Format the date to the desired format
    formatted_date = date_obj.strftime('%A %d %B %Y')
    
    return formatted_date

# Example usage
example_date = '2021-05-27 17:08:34.149Z'
print(get_str_date(example_date))  # Output: Thursday 27 May 2021

# або варіант gemini 
from datetime import datetime

def get_str_date(date):
  """
  Перетворює дату з бази даних у форматі ISO 
  '2021-05-27 17:08:34.149Z' у рядок 
  'Thursday 27 May 2021'

  Args:
    date: Дата в форматі ISO

  Returns:
    Рядок з датою у форматі 'день тижня число місяць рік'
  """
  # Перетворюємо дату ISO у формат datetime
  date_obj = datetime.fromisoformat(date)

  # Отримуємо день тижня
  day_of_week = date_obj.strftime("%A")

  # Отримуємо число
  day = date_obj.strftime("%d")

  # Отримуємо місяць
  month = date_obj.strftime("%B")

  # Отримуємо рік
  year = date_obj.strftime("%Y")

  # Формуємо рядок з датою
  str_date = f"{day_of_week} {day} {month} {year}"

  # Повертаємо рядок з датою
  return str_date

# Приклад використання
date_str = "2021-05-27 17:08:34.149Z"
str_date = get_str_date(date_str)
print(str_date) # Thursday 27 May 2021
