s = input("Enter a word: ")
print(s)
##for i in range(1, len(s)):
##    s = s[-1] + s[:-1]
##    print(s)

##for i in range(0, len(s)):
##    s = s[1:]
##    print(s)

for i in range(0, len(s)):
    s = s[1:-1]
    print(s)
