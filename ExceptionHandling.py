try:
    result = 2/0
except ZeroDivisionError:
    print('Division by 0 not possible')
else:
    print('Everything worked')
finally:
    result=1

print(result)

raise Exception('An error!')
