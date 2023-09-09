
# sets have no duplicates and are unordered


s1 = {'Vibhor','Priyank','Bhavya','Sid'}

s2 = {'Vibhor','Bhavya'}



su = s1 | s2 #union

si = s1 & s2 # intersection

sd = s1- s2 # difference

print(f'{su}\n{si}\n{sd}')

print(s1>s2) 
print(s1<s2)

print(list(s1))