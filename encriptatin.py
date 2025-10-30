import random
def xor_cifrar_desencriptar(texto):
    clave = [random.randint(0, 1) for _ in range(len(texto))]
    cifrado = ""
    desencriptado = ""
    for i in range(len(texto)):
        c = chr(ord(texto[i]) ^ clave[i])  
        cifrado += c
        desencriptado += chr(ord(c) ^ clave[i])  
    return cifrado, desencriptado, clave
texto = input("Ingrese el texto a cifrar: ")
cifrado, desencriptado, clave = xor_cifrar_desencriptar(texto)
print("Clave generada:", clave)
print("Texto cifrado:", cifrado)
print("Texto desencriptado:", desencriptado)
