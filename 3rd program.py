import random
arr=input("Enter The Message: ").strip()
print(chr(random.randint(65,81))+arr[::-1])