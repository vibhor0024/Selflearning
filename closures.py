def counter():
    count = 0
         
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

increased = counter()

print(increased())
print(increased())


print(type(increased))
