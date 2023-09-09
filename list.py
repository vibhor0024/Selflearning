courses = ['Art','Science','English','Math']

courses.insert(2,'Physics') # to insert a new entry at a specific index

courses.append('Chemistry') # to insert a value at the end

print(courses)

courses2 =['History','Business']

courses.extend(courses2) # to combine two lists

print(courses)

courses[1:3] = ['Economics','Physical','AI'] # to insert multiple values at an index

print(courses)

print(len(courses)) # prints the length of the list

courses.remove('Chemistry') # to remove an item

print(courses)

courses.reverse() # modifies the original list and puts it in reverse

print(courses)

courses.sort() # sorts the original list in ascending order 
               # but does uppercase first then lowercase

courses.sort(key=str.lower) # sorts properly

print(courses)

courses.sort(reverse=True) # sorts the original list in descending order

print(courses)

coursecopy = courses[:] # creating a copy of a list

courses += ['IAS','FOA'] # another way to add more items

print(courses)

print(courses.index('English')) # to print the index of the item

# List compression

number = [1,2,3,4,5]

double = [n*2 for n in number]

print(double)

