print("Hello World")
a = 5
print(a)
b = "Hi"
print(b)
c = [1, 2, 3]  # Values can be changed
print(c[2])
d = True
print(d)
e = (1, "Moshe", True)  # can't change values
print(e[1])
f = ["Nikita", "Green", 30, False]
g = {"First Name": "Nikita", "Last Name": "Green", "Age": 32, "isMarried": False}
h = [{"Name": "Nikita", "Age": 30}, {"Name": "Orel", "Age": 69}]
print(h[1]["Name"])
print(g['First Name'])
k = 'Hello' + ' World'
s = 'Hello'
m = 'World'
t = f"{s} {m}"  # Additional method to represent K
n = "%s %s" % (s, m)  # Additional method to represent K
print(k)  # \n - new line, \t - tab, \r - return to beginning
print(t)
print(n)
if a < 4:
    print(True)
else:
    print("a is smaller")
