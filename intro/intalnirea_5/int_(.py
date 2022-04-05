# Write a function that takes as argument a natural number and prints all numbers between 0 and itself
def to_number(nr):
    for elem in range(1, nr):
        print(elem)


to_number(5)


# Modify the previous function to return the numbers inside a list instead
# 1,2,3,4
def to_number(nr):
    my_list = []
    for elem in range(1, nr):
        my_list.append(elem)
    return my_list


l = to_number(5)  # ar trebui sa returneze [1,2,3,4]
print(l)

# Write a function that takes as argument a natural number x and an optional argument natural number y
#(that if not passed, takes as default value 2). The function which will print the result of x to the power y
# as a verbose f-string: "The result of x={} to the power of y={} is:{} "

def natural(x, y = 2):
    z = x**y
    print(f'The result of x={x} to the power of y={y} is:{z}')
natural(4)



def func(x, y=2):
    res = x ** y
    print(f'The result of x={x} to the power of y={y} is: {res}')


func(5, 3)

# Write a function that has one string argument and creates a substring made of the first, middle and last character of the string
# e.g.:  substring('Michael') => 'Mhl'
#        substring('Adrian')  => 'Arn' / 'Ain' (either one works)
def s(name):
    name_2=name[0]+name[len(name)//2]+name[len(name)-1]
    print(name_2)

s('Cristi')

# Given 2 strings as arguments s1 and s2, write a function that appends s2 in the middle of s1
# e.g.:  append_middle('Legendary', 'wait')  => 'Legewaitndary'
#        append_middle('mama', 'MIA')  =>  'maMIAma'

def append_middle(s1, s2):
    middle = len(s1)//2
    result_string = s1[0: middle] + s2 + s1[middle:]
    print (result_string)
append_middle('mama', 'MIA')
append_middle('Legendary', 'wait')

# Write a function that takes any number of string arguments and will return the string formed
# from the arguments separated by -
# e.g.: coma_separated('one', 'two', 'three') => 'one-two-three'
# coma_separated('one', 'two', 'three', 'four', 'five') => 'one-two-three-four-five'



