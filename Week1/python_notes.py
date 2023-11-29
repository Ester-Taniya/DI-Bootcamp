
#enumerate
for i,car in enumerate(list(range(10))):
    if car==5:
        print(i)

a,b,c,*other=[1,2,3,4,5,6,]
print(other)


l1=[1, 2, 3, 4, 5, 6]
l1.insert(2, 6)
print(l1)

print('------')

lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[0:4]) # from
print(lst[::])# all
print(lst[::-1])# reverse

print('------')

# TRIPLE not changrd
t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9)
t3 = t1 + t2 # can add
print(t3)
print(min(t3))
print(max(t3))

# *args do a tupple
# *kwargs do a dictinaris

'''
def combined_function(arg1, arg2, *args, **kwargs):
    print(f"Arguments: {arg1}, {arg2}")
    print(f"Additional positional arguments: {args}")
    print(f"Additional keyword arguments: {kwargs}")

combined_function("value1", "value2", "extra1", "extra2", key1="value1", key2="value2")

Arguments: value1, value2
Additional positional arguments: ('extra1', 'extra2')
Additional keyword arguments: {'key1': 'value1', 'key2': 'value2'}
'''
#clean code:
def is_even(num):
    return num % 2 ==0
print(is_even(50))


