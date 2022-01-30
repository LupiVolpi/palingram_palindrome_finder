import cProfile
import palingram_finder
import load_dictionary

loaded_dictionary = set(load_dictionary.load("dictionary.txt"))
cProfile.run(f"palingram_finder.find_palingrams({loaded_dictionary})")
