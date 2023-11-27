


user_str=input('give me a strinf 10 chr long:')

if len (user_str)<10:
    print ('string not long enoth') 
elif len (user_str)>10:
    print('string too long ')
else:
    print('perfect string') 

  #2___
    print(f'first characters "{string[0]}" ,the last  characters "{string[-1] }"')


    '''string = str(input("enter 10 characters long string"))

if len(string) < 10: 
    print('string  not long enough')
elif len(string) > 10: 
    print('string too long ')
else:
    print('perfect string') 

  #2___
    print(f'first characters "{string[0]}" ,the last  characters "{string[-1] }"')

  #3___
    #for i in range(len(string)):
    #   print(string[:i+1])
  
  
output_str= ''
for char in string:
    output_str




  #4___
    import random
    s_list=list(string)
    random.shuffle(s_list)
    shuffled_string=''.join(s_list)
    print(shuffled_string)
'''


list=[5,10,15,20,25,50,20]
for i in range(len(list)):
  if list[i]==20:
    list[i]=200
    break
print(list)






my_set= set()
my_set2= {60,14,"Morty"}
my_set.add("Rick")
my_set.add('Morty')
my_set.add("Rick")
print(my_set2)
inter=my_set.intersection(my_set2)
print(inter)
#dif=my_set.diference(my_set2)
#print(dif) ???????





#for loops
students=['Lior','Sveta','Esty','David']

for each_studens in students:
    if each_studens is 'Sveta':
        print("H-b day , Sveta")
    print(f'hello, {each_students}')


# for loop ex 
usser_num=int(input('write numer'))
for i in range(1,11):
    print(i*usser_num)




#while loop ex
count=1
while count <= 10:
    print(count)
    count += 1

#######

students=['Lior','Sveta','Esty','David']    
for i,j in enumerate(students):
    print(i,j)

