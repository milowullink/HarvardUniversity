from emoji import emojize

def convert(text):
    if ":)" in text:
        text = text.replace(":)", emojize(":slightly_smiling_face:"))
    if ":(" in text:
        text = text.replace(":(", emojize(":slightly_frowning_face:"))
    return text

text = input("What text would you like to convert? ")
print(convert(text))