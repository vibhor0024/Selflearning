from functools import reduce

multiply = lambda a,b : a*b # Lambda function
                            # no name
                            # only 1 expression as their body

print(multiply(2,3))
print(type(multiply)) #function

#Map

numbers = [1,2,3,4,5,6]

def double(a):
    return a*2

result = map(double, numbers) # a function to run the double function on every number in the list or a collection

#OR result = map(lambda a:a*2, numbers)
print(list(result))

print(type(result)) #map

#Filter

result2 = filter(lambda a: a%2 == 0, numbers )


print(list(result2))

#Reduce

expenses =[('dinner',80),('carwash',120)]
sum = 0
for expense in expenses:
    sum += expense[1]

print(sum)

sum2 = 0
sum2 = reduce(lambda a,b: a[1] + b[1],expenses)

print(sum2)