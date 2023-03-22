# from lynn
def decoder(password):
    res = ""
    for char in password:
        res += str(int(char) - 3)
    return res