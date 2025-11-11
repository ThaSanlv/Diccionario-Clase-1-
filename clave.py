import random
v = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

contraseña = int(input("¿De cuantos caracteres quiere la contraseña?"))

clave= ""

for i in range(contraseña):
    clave += random.choice(v)

print (clave)
