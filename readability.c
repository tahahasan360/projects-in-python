from cs50 import get_string

s = get_string("Text: ")
l = 0
w = 1
S = 0

for c in s:
    if c.isalpha():
        l += 1
    elif c == " ":
        w += 1
    elif c in {"?", "!", "."}:
        S += 1
        
L = l/w * 100  
S = S/w * 100
index = round(0.0588 * L - 0.296 * S - 15.8)
if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print("Grade " + str(index))
