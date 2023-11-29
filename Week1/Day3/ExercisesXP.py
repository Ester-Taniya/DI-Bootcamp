'''___Exercises XP_____________________________________________________________________________________________________________________________________'''
#____Exercise 1 : Convert Lists Into Dictionaries   _____

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict=dict(zip(keys,values))
print(dict)
#___________________________


#____Exercise 2 : Cinemax: _____
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_price=0
for name in family.keys():
    
    age= family[name]
    

    if age < 3 and age > 0:
      ticket_price = 0
    elif age >= 3 and age < 12:
       ticket_price = 10
    else:
        ticket_price = 15
    total_price+=ticket_price
    print(f' {name.capitalize()},you have to pay:  {ticket_price}  ')
print(f'The  family’s total price:  {total_price} ')

#bonuus:

family = dict()
print(family)
quit = "Q"

while True:

    name = str(input(F'please enter your Name(to quit print "Q") :')).capitalize()
    if name == 'Q':
        break
    age = input(F'and now enter your Age:')

    family[name]=int(age)
    print(family)
#___________________________






#____Exercise 3: Zara  _____________

#1 / #2
brand={
'name': 'Zara',
'creation_date': 1975,
'creator_name': 'Amancio Ortega Gaona',
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color': {'France': 'blue',
    'Spain': 'red',
    'US': ['pink', 'green']}
}


#3
brand['number_stores']=2


#4
print(f"""Zara's clients are people who want to buy goods for: {', '.join(brand['type_of_clothes'])},
and also shopping in the next stores : {', '.join(brand['international_competitors'])}. """)

#5

brand['country_creation']='Spain'

#6

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
    

#7
brand.pop('creation_date')

#8
brand['international_competitors'].pop() # /  brand['international_competitors']= brand['international_competitors'][0:-1]

#9
print(brand['major_color']['US']) # if need print  not as list:  print(', '.join(brand['major_color']['US']))

#10
print(len(brand))


#11
print(brand.keys())

#12

more_on_zara = brand
more_on_zara.update({'creation_date': 1975, 'number_stores': '10.000'}) # creation_date  = changed on the same  value ( brand had also1975 )


''' Another way to change value:

more_on_zara=brand
more_on_zara['creation_date']=1975
more_on_zara['creation_date']='10 000' # or = 10000 (like int)

'''
 
 #13
brand.update(more_on_zara)
# its jut changet information 

#14

print(brand['number_stores'])
# the output: 10 000

#__________________________________



#____Exercise 4 : Disney Characters _____
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

"""
#1/

>>> print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}


Answer: this tells us that there is a dictionary of creatures from the list users list where key: users item  value:  item index
disney_users_A = dict(zip(users, range(len(users)))) 

#2/

>>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
Answer: this tells us that there is a dictionary of creatures from the list users list where key: users item index  value: item 
disney_users_A = dict(zip( range(len(users), users)))
/ or changed disney_users_A dictionary:  disney_users_B = dict(zip(disney_users_A.values(), disney_users_A.keys()))



#3/

>>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
changed disney_users_A dictionary: 
 its look like random ordered list users:
 random.shuffle(users) # (import random in step before)
 disney_users_G = dict(zip(users, range(len(users)))) 
 
 
#__________________________
"""
#1
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}
for index,name in enumerate(users):
    disney_users_A[name]=index
print(disney_users_A)
"""
the hardcode way(if it is ):

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
indexes=[]
for i in range(0,len(users)):
    indexes.append(i)
disney_users_A = dict(zip(users, indexes))
print(disney_users_A)
print(enumerate(users))
"""
#2
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_B = {}
for index,name in enumerate(users):
    disney_users_B[index]=name
print(disney_users_B)

#3
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_C = {}
users.sort()
for index,name in enumerate(users):
    disney_users_C[name]=index
print(disney_users_C)

#4.1
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}
for index,name in enumerate(users):
    if 'i' in name:
        disney_users_A[name]=index
print(disney_users_A)

#4.2

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}
for index,name in enumerate(users):
    if name[0].lower() == 'm' or name[0].lower() == 'p':
        disney_users_A[name]=index
print(disney_users_A)

#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________


