#____Exercise 1 : Hello World____

print("Hellow World\n" *4)
# _________________________



#____Exercise 2 : Some Math____
print ((99**3)*8)

# _________________________



#____Exercise 3 : What Is The Output ?____

5 < 3 # FALSE
3 == 3 # TRUE
3 == "3" # FALSE
"3" > 3 # ERROR
"Hello" == "hello" #FALSE
# _________________________



#___ Exercise 4 : Your Computer Brand____
computer_brand="Apple"
print(f"I have a {computer_brand} computer. ")
# _________________________



#___ Exercise 5 : Your Information____
name = 'Esty'
age = 28
shoe_size = 38
info=f"Hi, my name is {name}, I'm {age} years old and my shoe size is {shoe_size}."
print(info)
# _________________________




#___Exercise 6 : A & B_____

a = 5
b = 1
if a>b: print("Hello World")
# _________________________



#_____Exercise 7 : Odd Or Even_____
number=int(input("what your number?"))
if number % 2 == 0:
    print("the number is even ")
else: print("the number is odd ")

# _________________________
###





#_______  Exercise 8 : What’s Your Name ?______
user_name=str(input("what your name?"))

short_name='Esty'
long_name='Ester'

if  user_name.capitalize() == short_name or long_name : # also we can use elif (but its not short way)
    print("How cool , Two Esty ")
else:  print("nooooo cool, IT'S NOT Tasty")

# ____________________________




#_______ Exercise 9 : Tall Enough To Ride A Roller Coaster ______

user_height= float(input("wrigt yor height in inches:"))
required_height=145                                         #(not not include, as I understand)
if user_height>required_height:                             #145 its No , 145.1 its OK
    print('You are tall enough to ride')
else: print('You are need to grow some more to ride')
# ____________________________






