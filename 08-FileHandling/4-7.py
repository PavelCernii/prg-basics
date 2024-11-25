import re

def count_vowels(text):
    vowels = re.findall(r'[aeiouAEIOU]', text)
    return len(vowels)

text = input("Enter a text: ")
num_vowels = count_vowels(text)
print(f"Number of vowels: {num_vowels}")
