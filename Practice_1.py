i = 0
sum = 0
while (i < 1000):
    if (((i % 3)== 0) or ((i % 5) == 0)):
        sum = sum + i
    i = i + 1

print("Answer 1 is " + str(sum))

i = 2
x = 1
z = 0
sum = 2
while (i < 4000000):
    z = i
    i = x + i
    x = z
    if ((i % 2) == 0):
        sum = sum + i

print("Answer 2 is " + str(sum))

       


