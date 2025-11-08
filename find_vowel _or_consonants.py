sentence = "the weather is beautiful"
vowel_count = 0
vowels = "a,e,i,o,u"
for letter in sentence:
    if letter in vowels:
        vowel_count += 1
        print(letter)
print("vowels count is",vowel_count)
