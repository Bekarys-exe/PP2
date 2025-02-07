def GrToOun(grams):
    return 28.3495231 * grams

grams = int(input("Grams: "))
print(f"Ounces: {GrToOun(grams)}")
ex = input("Press ENTER to exit")