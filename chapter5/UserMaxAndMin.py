times = int(input("how many number do you want to calculate\n "))
maxi = 0
# mini = float('inf')
mini = 99999999
for bone in range(times):
    first = int(input("please enter your number\n"))
    if first > maxi:
        maxi = first
    if first < mini:
        mini = first
print("this is max  ", maxi)
print("this is min  ", mini)
