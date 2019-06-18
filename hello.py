from sys import argv
if len(argv) > 1:
    message = " ".join(argv[1:])
else:
    message = "World"
print("Hello, {}!".format(message))