x = input()
y = input()

if x == "links" and y == "links":
   n = 5

if x == "links" and y == "evenwicht":
    n = 6

if x == "links" and y == "rechts":
    n = 4

if x == "evenwicht" and y == "links":
   n = 8

if x == "evenwicht" and y =="evenwicht":
    n = 9

if x == "evenwicht" and y == "rechts":
    n = 7

if x == "rechts" and y == "links":
   n = 2

if x == "rechts" and y =="evenwicht":
    n = 3

if x == "rechts" and y == "rechts":
    n = 1

print(f"muntstuk #{n} is vervalst")