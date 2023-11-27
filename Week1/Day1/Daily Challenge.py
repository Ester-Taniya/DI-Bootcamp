#_________Daily Challenge: Build Up A String______________________________________________

# 1___
string = str(input("enter 10 characters long string"))

if len(string) < 10: 
    print('string  not long enough')
elif len(string) > 10: 
    print('string too long ')
else:
    print('perfect string') 

  #2___
    print(f'first characters "{string[0]}" ,the last  characters "{string[-1] }"')

  #3___
    for i in range(len(string)):
        print(string[:i+1])


  #4___
     import random
    s_list=list(string)
    random.shuffle(s_list)
    shuffled_string=''.join(s_list)
    print(shuffled_string)

  
   
