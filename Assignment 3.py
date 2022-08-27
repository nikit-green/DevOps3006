from PIL import Image, ImageDraw

# 1 + 2
try:
    a = 1 / 0
except ZeroDivisionError as e:
    print(e.args)

# 3 - yes
try:
    x = 1
finally:
    print("finally")

# 4 - "except" cover all type of exception errors

# 5 - built-in except is too general there is also a chance that we get exceptions that we didn’t expect,
# and which we cannot recover from; or shouldn’t recover from.

# 6- It is an error raised when an input/output operation fails,
# such as the print statement or the open() function when trying to open a file that does not exist.

# ZeroDivisionError occurs when a number is divided by a zero. In Mathematics, when a number is divided by a zero,
# the result is an infinite number. It is impossible to write an Infinite number physically

# 7 + 8 + 9
my_file = open("words.txt", "w+")
my_file.write("Nikita")
my_file.seek(0)
for line in my_file.readlines():
    print(line)
my_file.close()
# 10
my_file = open("words.txt", "w+", encoding='UTF-8')
my_file.write("טקסט בעברית")
my_file.seek(0)
for line in my_file.readlines():
    print(line)
my_file.close()

# Challenge
img = Image.new('RGB', (100, 100), color=(73, 109, 137))
d = ImageDraw.Draw(img)
d.text((20, 20), "Hello World", fill=(255, 255, 0))
img.save('pil_text.png')
img.show()
