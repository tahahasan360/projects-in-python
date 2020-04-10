from math import ceil, floor
from cs50 import get_string

num = get_string("Number: ")
if int(num) < pow(10, 12) or int(num) > pow(10, 16) - 1:
    print("INVALID")
    exit(1)

n = len(num)
evendigits = floor(n/2)
odddigits = ceil(n/2)
x = 0
y = 0
for i in range(1, evendigits + 1):
    x += (floor(2 * int(num[n - (2 * i)]) / 10)) + ((2 * int(num[n - (2 * i)])) % 10)
for i in range(odddigits):
    y += int(num[n - (2 * i) - 1])
    
if ((x + y) % 10) == 0:
    if num.startswith(("34", "37")):
        print("AMEX")
        exit(0)
    elif num.startswith(("51", "52", "53", "54", "55")):
        print("MASTERCARD")
        exit(0)
    elif num.startswith("4"):
        print("VISA")
        exit(0)
else:
    print("INVALID")
    exit(0)
