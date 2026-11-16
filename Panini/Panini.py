# This is a dictionary of English words and their Turkish translations
words = {"cat": "kedi", "horse": "at", "bird": "kuş", "lion": "aslan"}
print(words["lion"])
print(len(words))

# Adding new word to the dictionary, and updating existing word
words.update({"fish": "balık"})
words.update({"cat": "kedicik"})
print(words)

# Adding two more words to the dictionary
words.update({"parrot": "papağan", "bat": "yarasa"})
print(words)

# Printing the keys, values, and items of the dictionary
print(list(words.keys()))
print(list(words.values()))
print(list(words.items()))