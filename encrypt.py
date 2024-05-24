import time, os, random, string

def getMessage():
    msg = input("Message: ")
    return msg

def encrypt():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    print(chars)
    chars = list(chars)
    
    key = chars.copy()
    random.shuffle(key)
    
    msg = getMessage()
    c_msg = ""
    
    s = int(input("Encryption: "))
    for i in range(s):
        for c in msg:
            index = chars.index(c)
            c_msg += key[index]
        msg = c_msg
        #print(i)
        #print(c_msg)
        if (i < s - 1):
            c_msg = ""

    key = "".join(key)
    
    k_msg = key + c_msg
    print(f"Message  : {msg}", end="\n\n")
    print(f"Key      : {key}", end="\n\n")
    print(f"c_Message: {c_msg}", end="\n\n")
    print(f"c_Message (with Key): {k_msg}")