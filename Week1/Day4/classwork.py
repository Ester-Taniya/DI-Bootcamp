#day 4 function:
''''
def  say_hallo(username,language):
   if language=="EN":
       print('say hallo'+username)
   elif language=="FR":
        print('say bonjor' + username)
   else: print('this language is nor sopousted:' + language)

   username='Rick'
   language='FR'


   say_hallo(username,language)
   say_hallo('Rick','FR')
   say_hallo(username='Rick',language='FR')
   say_hallo('Rick', language='FR')

#default value in argument

say_hallo(username='Rick',language 'FR')
'''


#global Scope
'''name='Avner'
def say_Hi():
    name = name.lower
    print(name)
say_Hi()
'''
"""""
def square(number:int)->int:
    num_squared = number**2
    return num_squared
print(square(2))

def countri_info(contry)-> tuple:
    if contry == 'Israel':
        population = 936400
        capital = 'Jerusalem'
    if contry == 'Russia':
        population =1434000000
        capital = 'Mosow'
    if contry == 'Brazil':
        population = 21430000000
        capital = 'Brasiliya'
    return  population,capital
print(countri_info('Israel'))
pop,cap = countri_info("Brazil")
a countri_info(Israel)
#print(f'the population is  {population}')

#Exercise----
'''
Write a function calculation() 
such that it can accept two variables and calculate the
 addition and subtraction of it. And also it must return both
  addition and subtraction in a single return call

For example:

def calculation(a, b):
    # Your Code
'''
res = calculation(40, 10)
print(res)
"""
def calculation(a,b):
    add=a+b
    subs=a-b
    return add,subs
result= calculation(2,1)
print(result)

#_________
print ('_________*Args And **Kwargs')
# _______________________________________________________________________________

'''

def prin_names(*args):
    for i in args:
        print(i)

# args=*
prin_names('David')




#kwargs =**
def print_info(**info):
    # pass
    print(kwargs['adress'])

print_info(name='Viktor', age= 25,adress ="Holon")
'''


def gamer_info(*args,**kwargs):
    print(max(args))
    print(kwargs)

gamer_info(150,123,544,534,name='john', l_name='Doe',age=23)

print('_________')


# *args do a tupple
# *kwargs do a dictinaris


def combined_function(arg1, arg2, *args, **kwargs):
    print(f"Arguments: {arg1}, {arg2}")
    print(f"Additional positional arguments: {args}")
    print(f"Additional keyword arguments: {kwargs}")

combined_function("value1", "value2", "extra1", "extra2", key1="value1", key2="value2")

print('------')
w='368817382'
w2=w.replace('8',"11")
print(w2)
print(w)


