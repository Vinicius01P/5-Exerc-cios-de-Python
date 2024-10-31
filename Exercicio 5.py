def inverterPalavras(frase):
    palavrasInvertidas = [palavra[::-1] for palavra in frase.split()]
    novaFrase = " ".join(palavrasInvertidas)
    return novaFrase

frase = input("Escreva uma frase: ")
novaFrase = inverterPalavras(frase)
print("Frase com as palavras invertidas:", novaFrase)
