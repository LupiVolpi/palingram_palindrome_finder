import sys


def load(file):
    try:
        with open(file) as in_file:
            loaded_dictionary = in_file.read().strip().split("\n")
            loaded_dictionary = [word.lower() for word in loaded_dictionary if len(word) > 1]

        return loaded_dictionary

    except IOError as e:
        print(f"{e}\nError opening {file}. Terminating program.")

        sys.exit(1)

dictionary = load("dictionary.txt")
print(dictionary)
