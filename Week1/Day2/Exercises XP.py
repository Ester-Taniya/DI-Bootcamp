'''___Exercises XP_____________________________________________________________________________________________________________________________________''''

#____ Exercise 1 : Set_____

#1
my_fav_numbers=set()
#2
my_fav_numbers.add("3")
my_fav_numbers.add("9")
print(my_fav_numbers)
#3
my_fav_numbers.pop()
print(my_fav_numbers)
#4
friend_fav_numbers={'7', '5','11'}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers) #we hawe set witout num "9", remowed it in step before

#___________________________




#____Exercise 2: Tuple   ______
'''no,you can't change Tuple,  because  they are immutamle '''
#___________________________




#____Exercise 3: List

basket = ["Banana", "Apples", "Oranges", "Blueberries"]



#1
basket.remove('Banana') # if we know index: basket.remove(basket[0])
print(basket)

#2
basket.remove('Blueberries')#if we know index: basket.remove(basket[-1]) or basket.pop()
print(basket)

#3
basket.append('Kiwi')
print(basket)

#4
basket.insert(1,'Apples')
print(basket)

#5
print(basket.count('Apples'))

#6
basket.clear()

#7
print(basket)

#___________________________








#____Exercise 4: Floats   ______
#1
''' the "int" its a whole numers, "float" its not whole numbers with a decimal point'''

#2
sequence=[]
x=0.5
while x <= 20:
    sequence.append(x)
    x += 0.5

print(sequence)

# 3
sequence=[]
x=1.5
while x <= 5:
    if x % 1 == 0:
        sequence.append(int(x))
    else:sequence.append(x)
    x += 0.5
print(sequence)


#___________________________




#____Exercise 5: For Loop   ______

#1
for i in range(1,21):
    print(i)

#2
list=[]
for num in range(1,21):
    list.append(num)

for i in list:
    if list.index(i) %2 == 0:
        print(i)



#___________________________





#____Exercise 6 : While Loop  ______
my_name = "Esty"
user_name = str(input("please enter your name:"))
while my_name != user_name.capitalize():
    user_name = str(input("sorry,try again:")).capitalize()
print('your name equal to my name')

#___________________________




#____Exercise 7: Favorite Fruits  ______

#1
fruits=str(input("""print your favorite fruit(s), on 1 line 
and separate the fruits with a single space 
example: 'apple mango cherry' : """))

#2
Fruits_list=fruits.split()

#3
user_fruit=str(input('enter a name of any fruit:'))
if user_fruit in Fruits_list:
    print('You chose one of your favorite fruits! Enjoy!')
else: print('You chose a new fruit. I hope you enjoy')

#___________________________






#____Exercise 8: Who Ordered A Pizza ?   ______

#1
topping=str(input(""" Hi, please enter a name of topping what you want to order:
( to stop order print 'quit' ) """))
pizza =[]

pizza.append(topping)

while topping != 'quit':

    topping=str(input("""this topping add to pizza
    what else?"""))
    pizza.append(topping)

#3
pizza_s=','.join(pizza)

print(f'So, now  in your pizza {pizza_s}, and total price: {10+(2.5*(len(pizza)-1))}') # or  insted '10' and '2.5'  we can add varible "pizza_price=10" and "topping_price=2.5"


#___________________________




#____Exercise 9: Cinemax  ______

#1
total_price = 0
age = int(input("""enter a person  age: 
(of the end  enter  '0') """))


if age < 3 and age > 0:
    ticket_price = 0
elif age >= 3 and age < 12:
    ticket_price = 10
else:
    ticket_price = 15


total_price += ticket_price #3

#2
while age != 0:
    age = int(input(('ok, ticket added,what the next person age?')))

#3
print(f'The total cost of all the family’s tickets: {total_price} dolars ')


# 4
group=['Tom','Anna','Joe', 'Ben', 'Jane']
new_group=[]
for i in group:
    age = int(input( f'{i}, please enter your age:'))
    print(i)
    if age not in range(16, 22):
        new_group.append(i)

print(new_group)
#___________________________




#____Exercise 10 : Sandwich Orders ______

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

#1
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

#2
finished_sandwiches=[]
while len(sandwich_orders)!= 0:
    finished_sandwiches.append(sandwich_orders[0])
    print(f'I made your {sandwich_orders[0]}') #3
    sandwich_orders.remove(sandwich_orders[0])

#or we can use varible 'current_sandwich':
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches=[]
while len(sandwich_orders)!= 0:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich[0])

#3
print(f'I made your {current_sandwich}')

#___________________________




'''_____________________________________________________________________________________________________________________________________'''



