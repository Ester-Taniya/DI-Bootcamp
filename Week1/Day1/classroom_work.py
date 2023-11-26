my_age=28
now=2023
year=123879
print(my_age+(year-now))

first_name='Esty'
last_name='Bobylea'
print(first_name+' '+last_name)

#---------------------------------------------------------------------------

#For example,
my_name = "Frank"  #this line creates a name variable type: string
print("My name is {}".format(my_name))

cars = 100 # this line creates Quantity of cars variable,type: int
space_in_a_car = 4.0 # this line creates a  Quantity space in a car variable,type: float
drivers = 30 # this line creates Quantity of drivers variable,type: int
passengers = 90 # this line creates a Quantity passengers of drivers variable,type: int
cars_not_driven = cars - drivers # this line creates a Quantity cars witout drivers variable,type: int
cars_driven = drivers # this line creates a Quantity cars with drivers variable,type: int
carpool_capacity = cars_driven * space_in_a_car  #type: int
average_passengers_per_car = passengers / cars_driven #type: int


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
