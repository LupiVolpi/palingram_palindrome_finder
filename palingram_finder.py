
########################################################################################################################
# Main program

import load_dictionary


def main():
    introduce_program()

    loaded_dictionary = load_dictionary.load("dictionary.txt")
    loaded_dictionary = set(loaded_dictionary)

    palingram_list = find_palingrams(loaded_dictionary)
    palingram_list = sort_palingrams(palingram_list)

    print_palingrams(palingram_list)

def find_palingrams(dictionary):
    print("Searching for palingrams, please wait...")

    palingram_list = []

    for word in dictionary:
        end_of_word= len(word)
        reversed_word = word[::-1]

        if end_of_word > 1:
            for index in range(end_of_word):
                if word[index:] == reversed_word[:end_of_word-index] and reversed_word[end_of_word-index:] in dictionary:
                    palingram_list.append((word, reversed_word[end_of_word-index:]))
                if word[:index] == reversed_word[end_of_word-index:] and reversed_word[:end_of_word-index] in dictionary:
                    palingram_list.append((reversed_word[:end_of_word-index], word))

    return palingram_list

def introduce_program():
    print("Welcome to the palingram finder!!")
    print("palingrams are sentences that look the same when reversed.")
    print("This program will help you find two-word palingrams!")
    input("Press enter to find palingrams ----> ")

def print_palingrams(palingram_list):
    print(f"\nNumber of palingrams found: {len(palingram_list)}\n")

    for first_word, second_word in palingram_list:
        print(f"{first_word} {second_word}")

def sort_palingrams(palingram_list):
    return sorted(palingram_list)

if (__name__ == "__main__"):
    main()

########################################################################################################################
# The Pseudocode
#
# Load a digital dictionary as a list of words
# Start an empty list to hold palingrams
# For each word in word list:
# Get length of word
# If length > 1:
# Loop through the letters in the word:
# If reversed word fragment at front of word is in word list and letters after form a palindromic sequence:
# Append word and reversed word to palingram list
# If reversed word fragment at end of word is in word list and letters before form a palindromic sequence:
# Append reversed word and word to palingram list
# Sort palingram list alphabetically
# Print word-pair palingrams from palingram list
