def file_opr(choice):
    f1 = open("sample.txt", "r")
    content = f1.read()
    print(content)

    if choice == "a":
        content = content.replace(".", ",")
    if choice == "b":
        content = content.upper()
    if choice == "c":
        content = content.lower()

    f2 = open("newfile", "w")
    f2.write(content)
    print("modified content store in new file")
    f2 = open("newfile", "r")
    print("New File content are")
    print(content)


choice = input("enter your choice")

print("press a for replacement")
print("press b for uppercase")
print("press c for lowercase")
print("press any other key to exit")

while choice in "abc":
    choice = input("enter your choice")
    if choice in "abc":
        file_opr(choice)

    else:
        print("exitting")
        break