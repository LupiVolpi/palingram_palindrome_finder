
########################################################################################################################
# Main program

import load_dictionary

def main():
    introduce_program()

    loaded_dictionary = load_dictionary.load("dictionary.txt")

    palindrome_list = find_palindromes(loaded_dictionary)

    print_list(palindrome_list)

########################################################################################################################
# Functions list

def find_palindromes(list):
    palindrome_list = []

    for word in list:
        if len(word) > 1 and word == word[::-1]:
            palindrome_list.append(word)

    return palindrome_list

def introduce_program():
    print("Hello and welcome to the palindrome finder!")
    print("Palindromes are words that look the same as normal when spelled backwards!!")
    input("Press enter to find palindromes --->")

def print_list(list):
    print(f"\n{len(list)} palindromes have been found!\n")
    print(*list, sep="\n")

if(__name__ == "__main__"):
    main()

########################################################################################################################
# The Pseudocode:
# Load a digital dictionary file as a list of words
# Create an empty list to hold palindromes
# Loop through each word in the word list:
# If the word sliced forward is the same as word sliced backwards, add the word to the palindrome list
# Print the palindrome list

