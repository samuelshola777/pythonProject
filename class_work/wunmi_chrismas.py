def day1():
    print("[Verse 1]\n" +
          "On the first day of"
          " Christmas, "
          "\nmy true love sent to me\n" +
          "A partridge in a pear tree\n")


if __name__ == '__main__':
    day1()
    list_samuel = []
    for x in range(1,10):
        list_samuel.append(x)
    print(list_samuel)


    list_samuel = [x for x in list_samuel if "a " in x]
    print(list_samuel)



    list_samm = [x for x in range(10,-1, -1)]
    print(list_samuel)

    wunmi = ["boneshaker", "samuel shola ", "mattaer "]
    print(wunmi)
