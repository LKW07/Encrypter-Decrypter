import time, os, random, string

def decrypt():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    ch_len = len(chars)
    chars = list(chars)
    
    c_msg = input("Encrypted Message: ")
    msg = ""
    
    key = input("Key: ")
    
    if not key and not c_msg:
        k_msg = input("Message with key: ")
        n_msg = k_msg
        c_msg = k_msg[ch_len:]
        c_len = len(c_msg)
        key = n_msg[:ch_len]
        #print(key, end="\n")
        #print(c_len)
        #print(c_msg)
        
    s = int(input("Decryption: "))
    key = list(key)
    for i in range(s):
        for c in c_msg:
            index = key.index(c)
            msg += chars[index]
        c_msg = msg
        if (i < s - 1):
            msg = ""
    
    key = "".join(key)
    #print(f"c_Message: {c_msg}")
    #print(f"Key      : {key}\n")
    print("\n\n")
    print(f"Message  : {msg}")