# Daily Challenge : Lists & Strings_____________________________________________________________________________________________________________________________________

#________Challenge 1 ________



number = int(input(('please,enter yor number:')))
length =int(input(('and enter length:')))
num_list=[]



for i in range(1,(length+1)):
    current_num = number*i
    num_list.append(current_num)


print(f'number: {number} - length {length } ➞ {num_list}')

#___________________________



#________Challenge 2 ________


string = str(input(('please,enter yor string:')))
new_string = ''
numbers=1

for i in string:
    if i not in new_string:
        new_string += i

print(f" user's word : '{string}'  ➞  '{new_string}'")

