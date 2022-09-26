def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)


def multiply(num_list, num):
    print(num_list, num)
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# # output:
# >>>[2,4,10,16] 5
# >>>[2,4,10,16]


def multiply(num_list,num):
    print(num_list, num)
    for x in num_list:
        print(x)
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# # # output:
# # >>>[2, 4, 10, 16] 5
# # >>>2
# # >>>4
# # >>>10
# # >>>16
# # >>>[2, 4, 10, 16]


def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(x)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# # output:
# >>>[2,4,10,16] 5
# >>>2
# >>>10
# >>>4
# >>>20
# >>>10
# >>>50
# >>>16
# >>>80
# >>>[2, 4, 10, 16]

def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# # output:
# >>>[2, 4, 10, 16] 5
# >>>2
# >>>[2, 4, 10, 16]
# >>>4
# >>>[2, 4, 10, 16]
# >>>10
# >>>[2, 4, 10, 16]
# >>>16
# >>>[2, 4, 10, 16]


def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# # # output:
# # >>>[10,20,50,80]










