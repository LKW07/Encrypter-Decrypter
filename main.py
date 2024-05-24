from encrypt import *
from decrypt import *

os.system("cls")
print("------------MENU--------------")
print("(1) Encrypt Message")
print("(2) Decrypt Message")
print("(3) Exit Programm")

c = input("> ")

os.system("cls")

match c:
    case "1":
        encrypt()
    case "2":
        decrypt()
    case "3":
        exit