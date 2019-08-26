"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()
word_definitions["nefarious"] = "Infamous by way of being extremely wicked"
word_definitions["fastidious"] = "Showing or acting with careful attention to detail"
word_definitions["avuncular"] = "Of or pertaining to an uncle"

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["nefarious"])
print(word_definitions["avuncular"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (key, value) in word_definitions.items():
    print(f"the definition of {key} is {value}")