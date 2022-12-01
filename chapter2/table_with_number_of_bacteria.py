#starting with 200 bacteria, the growth in the number
#of bacteria after n hour is calculated as B = 200 * 2 raise power of hour
print("hour            number of bacteria")
for n in range(0, 16, 5):

    bone = 200 * 2 ** n

    print(n,"<----------------------->",bone)
    