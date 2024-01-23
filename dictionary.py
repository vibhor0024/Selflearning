student = {'name':'Vibhor','age':24,'location':'Arizona','height':172}

print(student.pop('age')) # to remove a specific key value pair

print(student.popitem()) # removes the last item

print(student)

print(list((student.keys()))) # list of all the keys
print(type(student.keys()))
print(list(student.values())) # list of all the values

print(list(student.items())) # list of tuples with all key, value pairs

for k,v in student.items():
    print(k,v)


studentcopy = student.copy() # to make a copy

del student['name'] # deletes the name

print(student)
