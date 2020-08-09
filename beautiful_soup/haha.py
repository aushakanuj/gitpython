f = open("test.py", "r")

lines = f.read()

res = "".join(format(ord(i), "b") for i in lines)

image = open("hahahaha.bin", "w")
image
