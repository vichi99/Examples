rot = int(input("Enter rotation: "))
action = input("Do you want [e]ncrypt or [d]ecrypt data?: ")
data = input ("Enter text: ")
start, end = 32, 126 # chars in ascii for caesar cipher
divide = end - start

if action == "e" or action == "encrypt":
    text = ""
    for char in data:
        char_c = ord(char)
        if start <= char_c <= end:
            char_c -= start
            char_c += rot # encrypt
            char_c %= divide
            char_c += start
            text += chr(char_c)
        else:
            text += char
    # second solution
    #     symbol = ord(char) + rot
    #     if symbol > 122:
    #         symbol = symbol - 122
    #         symbol = symbol + 64
    #
    #     symbol = chr(symbol)
    #     text += symbol
    print("Text '{}' => '{}'".format(data,text))

elif action == "d" or action == "decrypt":
    text = ""
    for char in data:
        char_c = ord(char)
        if start <= char_c <= end:
            char_c -= start
            char_c -= rot # decrypt
            char_c %= divide
            char_c += start
            text += chr(char_c)
        else:
                text += char
    print("Text '{}' => '{}'".format(data,text))
else:
    print("Error with input")
