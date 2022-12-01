if __name__ == '__main__':
    temp_file = open("temp.txt","r")
    print("my name is samuel shola, i'm an english person and i live in bariga ", file=temp_file)
    print("second line ", file=temp_file)
    temp_file.close()

    vowels = ["a", "e", "i", "o", "u"]
    temp_file = open("temp.txt", "r")
    for samuel_shola in temp_file:
        for samuel_shola_guitar in samuel_shola:
            samuel_shola_guitar.strip().lower()
            vowels_of_the_word = []
            for boneshaker in samuel_shola_guitar:
                if boneshaker in vowels:
                    vowels_of_the_word.append(boneshaker)
            if vowels_of_the_word == vowels:
                print("Vowels of the word")
