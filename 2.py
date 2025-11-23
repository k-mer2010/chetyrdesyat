import random

chars = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
dlina = int(input("введите длину пароля"))
password = ''
a = 0
while a<dlina:
    password += random.choice(chars)
    a = a+1
print(password)
