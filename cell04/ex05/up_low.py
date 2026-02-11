word = input()
x = 0
check =""
while x < len(word):
    if(word[x] == word[x].upper()) :
        check += word[x].lower()
    else :
        check += word[x].upper()
    x += 1
print(check)