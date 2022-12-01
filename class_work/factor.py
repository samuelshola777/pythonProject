if __name__=='__main__':

    bone = int(input("please enter a number: "))
    tom = 0
    for z in range(1, bone):
        if bone % z == 0:
            print(z)
            tom += z
    print(tom)
