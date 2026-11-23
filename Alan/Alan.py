word = "bus"
irregular_plural = {"child": "children", "mouse": "mice"}
if word in irregular_plural:
    plural = irregular_plural[word]
    print(plural)
elif word.endswith(("s", "x", "z")):
    print(word + "es")
elif word.endswith("y") and word[-2] not in 'aeiou':
    print(word[: -1] + "ies")
else:
    print(word + "s")