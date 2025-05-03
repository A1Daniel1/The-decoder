def main():
    entrada = input("Digite a string a ser decifrada: ")
    resultado = ""
    for i in range(len(entrada)):
        if entrada[i].isalpha():
            if entrada[i].isupper():
                resultado += chr((ord(entrada[i]) - 65 - 3) % 26 + 65)
            else:
                resultado += chr((ord(entrada[i]) - 97 - 3) % 26 + 97)
        else:
            resultado += entrada[i]
    print("A string decifrada é:", resultado)   

if __name__ == "__main__":
    main()