'''
Student Name: Shlok Satish Nagare.
Roll No.: 39
Div: O
Assignment no: 5
Assignment type: Copying content from one file to another file and performing following tasks
'''
def file_opr(choice):
    f1 = open("sample.txt", "r")
    content = f1.read()
    print(content)

    if choice == "a":
        content = content.replace(".", ",")
        content = content.replace(":", ";")
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


choice = input("enter your choice\n")

print("press a for replacement\n")
print("press b for uppercase\n")
print("press c for lowercase\n")
print("press any other key to exit\n")
choice2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
while choice in choice2:
    choice = input("enter your choice\n")
    if choice in "abc":
        file_opr(choice)

    else:
        print("exitting")
        break

