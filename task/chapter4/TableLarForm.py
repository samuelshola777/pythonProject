def tablelar_form(numbr_Of_Table):
    for i in range(1,numbr_Of_Table):
        print(i, "    ", i * i, "   ", i * i * i, "   ", i * i * i * i, )

if __name__ == '__main__':
    
    tablelar_form(6)