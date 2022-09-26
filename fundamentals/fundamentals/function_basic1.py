#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# output:5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) # not defined
#output:error message

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#output:5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#output:5

#5
def number_of_great_lakes():
    print(5) #output:5
x = number_of_great_lakes()
print(x)
#output:5 none

#6
def add(b,c):
    print(b+c) #output:3 5
print(add(1,2) + add(2,3))
#output:error

#7
def concatenate(b,c):
    return str(b)+str(c)
    print(concatenate(2,5))

# 8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b) 
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents()) #output 100,10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #output 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #output 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #output 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# output 8

#11
b = 500
print(b) #output 500
def foobar():
    b = 300
    print(b) #output 500/
print(b) #output 300/
foobar()
print(b) #output500



#12
b = 500
print(b) #output 500
def foobar():
    b = 300
    print(b) #output 500? 
    return b #outout 300
print(b) #output 300?
foobar()
print(b) #Output 500?

#13
b = 500
print(b) #output 500
def foobar():
    b = 300
    print(b) #output 500
    return b #output 300
print(b)#output 300
b=foobar()
# print(b)# output 500

#14 
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# output : 1,3,2

#15
def foo():
    print(1) # 1
    x = bar() 
    print(x) #output 3,5
    return 10 
def bar():
    print(3) 
    return 5 
y = foo()
print(y)

# output : 1,3,5,10



