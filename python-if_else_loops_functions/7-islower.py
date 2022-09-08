def islower(c):
    ascci = ord(c)
    if (ascci >= 97 and ascci <= 122):
        ascci = 0
        return True
    else:
        ascci = 0
        return False
