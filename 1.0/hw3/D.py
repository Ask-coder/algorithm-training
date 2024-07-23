import sys
text = []
for line in sys.stdin:
    text += line.split()
print(len(set(text)))