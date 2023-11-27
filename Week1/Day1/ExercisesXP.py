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










#_______________Exercises XP Gold_________________________________________________________________________________________________________________________

#_______Exercise 1 : Hello World-I Love Python _____

print("Hellow World\n"*4,"I love python\n"*4)
#_________________________




#_______Exercise 2 : What Is The Season ? _____
number=int(input("write a number of the month(from 1 to 12)"))

while number <1 or number>12:
    print('Ooops! That was wrong number, try again...')
    number=int(input("write again (from 1 to 12)"))
if number==3 or number==4 or number ==5:
    print("this is Spring")
elif number ==6 or number==7 or number==8:
    print("this is Summer")
elif number==9 or number==10 or number==11:
    print("this is Autumn")
else: print("this is Winter")
#_________________________













#_______________Exercises XP Nija_________________________________________________________________________________________________________________________


#_______ Exercise 1 : Use The Terminal   _______
#The PATH variable in the operating system specifies where to find executable files.
# When you enter a command, the system uses PATH to locate and run the required file, 
#enabling the execution of commands like python3 from any directory in the terminal.
#
#_________________________





#_______Exercise 2 : Alias    _______
#An alias is a user-defined shortcut for a longer command
#example:
# '$ py'  for  '$ python3'


#_________________________





#_______ Exercise 3 : Outputs   _______
    >>> 3 <= 3 < 9     #True 
    >>> 3 == 3 == 3    #True
    >>> bool(0)        #False
    >>> bool(5 == "5")  #False
    >>> bool(4 == 4) == bool("4" == "4")    #True
    >>> bool(bool(None))    #False

    x = (1 == True)
    y = (1 == False)
    a = True + 4
    b = False + 10

    print("x is", x)     #x is True
    print("y is", y)    #y is False
    print("a:", a)    #a: 5
    print("b:", b)    #b: 10


#_________________________




#_______Exercise 4 : How Many Characters In A Sentence ?   _______
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
           
print(f" In this sentence {len(my_text)} characters")
#_________________________


#_______Exercise 5: Longest Word Without A Specific Character _______


text = str(input('Write the longest sentence you can without the character "A": '))
character = 'A'

if character not in text :  # if we also ban "a", need to add: "and character.lower()not in text"
    print("Congratulations, you wrote it all without 'A'.")
    
else:
    print('Sorry, try again.')
    text = str(input('at this time write your sentence cerfuly: '))
#_________________________







