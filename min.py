smallest = None
count = 0
print("Before:", smallest)
for itervar in [3100, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    count += 1
    print("Loop", str(count)+ ":", itervar, smallest)
print("Smallest:", smallest)

name = "Bu ngoo"
print("Ten t\n la: \t", name)
print('Ten t\n la: \t', name)
#cmt trong python
#cmt 2

