# 1.Basic - Print all integers from 0 to 150.

# for i in range (0,151):
#     print(i)

# 2.Multiples of Five - Print all the multiples of 5 from 5 to 1,000

# for i in range (5,1005,5):
#     print(i)

# 3.Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"/.

# def counting_dojo():
#     for i in range (1,101,1):
#         print(i)
#         if i % 10 ==0:
#             print ("Coding Dojo")
#         elif i % 5 ==0:
#             print("Coding")

# counting_dojo()

# 4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

# min = 0
# max = 500000
# oddtotal = 0

# for i in range(min, max+1):
#     if (i % 2!= 0):
#         print("{0}".format(i))
#         oddtotal = oddtotal+i

# print("The Sum of odd Numbers from {} to {} = {}".format(min,max,oddtotal))

# 5.Print positive numbers starting at 2018, counting down by fours.

# def countdown_by_four():
#     number = 2018
#     while number > 0:
#         print (number)
#         number =number - 4

# countdown_by_four()

# 6.Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

# def countdown(low,high,mult):
#     for i in range(low,high):
#         if i % mult ==0:
#             print(i)

# countdown(2,12,3)


