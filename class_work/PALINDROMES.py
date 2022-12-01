def palindrome():
    word = input("please enter a word ")
    word = word.lower()
    reverse = word[::-1]
    print(reverse)
    if reverse == word:
        print("the word is a palindrome")
    else:
        print("the number is not a palindrome ")


if __name__ == '__main__':
    palindrome()
