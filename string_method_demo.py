#lower

original = "Hello world"
lowered = original.lower()
print("Lowercase:",lowered)

#upper
uppered = original.upper()
print("Uppercase",uppered)

#strip method
messy = " python "
cleaned = messy.strip()
print("After strip:",cleaned)

#replace method
text ="Java is powerful"
updated = text.replace("java","python")
print("After replace:",updated)

#split() method
sentence="python is easy to learn"
word =  sentence.split()
print("split result:",word)

#find()  method
text = "learning python is fun"
position = text.find("python")
print("Found at index:",position)

#title() method
heading= "Welcome to python programming"
formatted=heading.title()
print("Title case:",formatted)

#capitalize()method
msg="hello WORLD"
cleaned=msg.capitalize()
print ("capitalized:",cleaned)

#starts with() method
greeting="hello everyone"
print(greeting.startswith("hello"))
print(greeting.startswith("hi"))

#ends with method
print(greeting.endswith("everyone"))
print(greeting.endswith("hello"))

#count()method
sentence="python is easy python is powerful,python is popular"
count=sentence.count("python")
print("total count:",count)

#is alpha method
name="python"
print(name.isalpha())
mixed= "python 3"
print(mixed.isalpha())

#isdigit () method
num =("205")
print(num.isdigit())

bad_input = "year2025"
print(bad_input.isdigit())

#isalnum() method
code ="abc123"
print(code.isalnum())

value = "abc123"
print(value.isalnum())

#join() method
words = ["pyhon","is","awesome"]
result ="".join(words)
print(result)

