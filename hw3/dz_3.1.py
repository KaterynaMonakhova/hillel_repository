import random
default_str = "abcdefjhijklmnopqrstuvwxyz"
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
for symbol in default_str:
    if symbol in consonants:
        default_str = default_str.replace(symbol, random.choice(vowels))
print(default_str)
