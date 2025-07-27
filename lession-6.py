# compare 
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
if x > y:
    print(x, "is greater than", y)
elif x < y:
    print(y, "is greater than", x)
else:
    # this is the else block, Example: x=5 and y=5
    print(x,"and", y ,"are equal")

# Logic operators
print(x > 0 and y == 0) # True if both are true
print (x > 0 or y == 0) # True if one of them is true
print(not(x>0)) # True if x is not true
