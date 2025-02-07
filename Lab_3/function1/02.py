def FToC(F):
    return (5 / 9) * (F - 32)

F = int(input("Fahrenheit: "))
print(f"Centigrade: {FToC(F)}")
ex = input("Press ENTER to exit")