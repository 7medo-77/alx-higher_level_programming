age = 25
name = "Ahmed"
profession = "dentist"
sentence = "this is a sentence to be manipulated with the string methods in python"
part = sentence[:25]
multi_string = '''This is a multiline string
continuation of the multi line string'''
delim = ("--" * 25) + "\n"

print(f"My name is: {name},\nI am {age} years old \nI am a {profession}")
print("\nMy name is: {},\nI am {} years old \nI am a {}".format(name, age, profession))
print("\nMy name is" + name + "\n I am" + str(age) + "years old" + "\n I am a " + profession)
print(f"\nthis is the sliced sentence to be printed: {sentence[:21]}")
print(f"\nthis is the sliced sentence to be printed: {sentence[21:]}")
print(delim + "My name is " + name + "\nI am a " + profession + "\n" + delim)
