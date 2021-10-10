s = input("Enter String : ")

if s == ''.join(reversed(s)):
    print(f"{s} is Palindrome")
else:
    print(f"{s} is not Palindrome")


print(f"Number of Characters in {s} : {len(s)}")
vowels = ['a','e','i','o','u']
n_vowels = 0
n_spaces = 0
for ch in s:
    if ch in vowels:
        n_vowels += 1
    if ch is ' ':
        n_spaces += 1

print(f"Number of Vowels in {s} : {n_vowels}")
print(f"Number of Spaces in {s} : {n_spaces}")