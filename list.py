courses = ['Art','Science','English','Math']
courses.insert(2,'Physics')
courses.append('Chemistry')
print(courses)
courses2 =['History','Business']
courses.extend(courses2)
print(courses)
courses[1:3] = ['Economics','Physical','AI']
print(courses)
print(len(courses))
courses.remove('Chemistry')
print(courses)
courses.reverse()
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)


