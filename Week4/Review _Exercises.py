

#1. Write code that gets three words from a user and inputs them into a sentence using F-Strings.

def gets_three_words():
    w_list=[]
    while len(w_list) < 3:
        word = input("enter you word:")
        w_list.append(word)
    sentence=f"{w_list[0]} {w_list[1]} {w_list[2]}!"
    print(sentence)
#gets_three_words()


#2. Exercise: Write a list that contains 2 strings. Print the second string in uppercase and then the first string backwards.
list=['first','second']
print(list[1].upper())
print(list[0][::-1])


#____loops

#8 Exercise: Write a loop to print every number between 10 and 20.
number=10
while number <20:
    print(number)
    number += 1
    
#9. Exercise: Write a loop to print every odd number between 1 and 20