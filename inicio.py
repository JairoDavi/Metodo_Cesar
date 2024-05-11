def cifrado_cesar(texto, desplazamiento):
    return ''.join(chr(((ord(c) - 65 + desplazamiento) % 26) + 65) if c.isalpha() else c for c in texto.upper())

if __name__ == "__main__":
    texto_original = input("Ingrese el texto a encriptar: ")
    desplazamiento = int(input("Ingrese el desplazamiento para el cifrado César: "))
    
    texto_encriptado = cifrado_cesar(texto_original, desplazamiento)
    print("Texto encriptado:", texto_encriptado)

    texto_desencriptado = cifrado_cesar(texto_encriptado, -desplazamiento)
    print("Texto desencriptado:", texto_desencriptado)
