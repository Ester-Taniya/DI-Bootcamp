# Данные
total_events = 150
bad_outcomes = 12

# Расчет доли плохих исходов
percentage_bad_outcomes = (bad_outcomes / total_events) * 100

# Расчет доли хороших исходов
percentage_good_outcomes = 100 - percentage_bad_outcomes

# Вывод результатов
print(f"Общее количество событий: {total_events}")
print(f"Количество плохих исходов: {bad_outcomes}")
print(f"Доля плохих исходов: {percentage_bad_outcomes:.2f}%")
print(f"Доля хороших исходов: {percentage_good_outcomes:.2f}%")
