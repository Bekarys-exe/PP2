class StrMnp:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())

stringManip = StrMnp()
stringManip.getString()
stringManip.printString()
ex = input("Press ENTER to exit")