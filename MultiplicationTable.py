
for x in range (1, 11):
    for y in range (1, 11):

        print (x, 'x', y, '=', x*y)

print("")
print ("In order to avoid x*y = y*x : ")
print("")

for x in range (1, 11):
    for y in range (x, 11):
        print(x, 'x', y, '=', x * y)

