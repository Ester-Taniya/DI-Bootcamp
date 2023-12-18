from alert_each_city import City 


# Greeting the user
print("Hello! Welcome to the Alert Predictor!")
print("DISCLAIMER: This program provides the probability of an air raid based on alarm history.")
print("ALL INFORMATION IS ADVISORY.")

# Asking for the city name
city_name = input("Enter the name of your city: ")

city = City(city_name, 0, 0)


city_id = city.show_city()
if city_id is not None:
    print(f'let see what hapen in {city_name}')
    time= int(input("Enter number (0-24) of hour what you want to cheack :  "))
elif city_id is None:
    print(f'sorty,the {city_name} not finde maby you mean :')
    city.show_list_cities()
else:print('sorty,somfing wrong try in next time')

while time not in range(0,24):
    print('sorry wrong input')
    time=int(input('enter a hour number :'))


city_cheak=City(city_name, city_id, time)

total_alerts_in_hour = city_cheak.all_alerts_in_cities()
city_hour_alerts=city_cheak.hour_alerts_in_city()

percentage_alerts_outcomes = (city_hour_alerts / total_alerts_in_hour) * 100

if 10 < percentage_alerts_outcomes< 30:
    print('its will be prity good hour')
elif 30 < percentage_alerts_outcomes < 50:
    print('its will be quite a quiet hour')
elif 50 < percentage_alerts_outcomes < 70:
    print('there is a possibility of an air raid')
else: print('be careful,maybe you should consider staying home')



 