import math
import time

number = int(input("Write your number please: "))
miliseconds = int(input("Write your miliseconds time please: "))

time.sleep(miliseconds / 1000)

result = math.sqrt(number)

print("Square root of" , number ,  "after" , miliseconds ,  "miliseconds is" , result)