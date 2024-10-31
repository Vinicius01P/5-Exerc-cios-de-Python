def conversaoIdade(diasTotais):
    anos = diasTotais // 365
    diasRestantes = diasTotais % 365
    meses = diasRestantes // 30
    dias = diasRestantes % 30
    return anos, meses, dias

diasTotais = int(input("Insira a sua idade em dias: "))

anos, meses, dias = conversaoIdade(diasTotais)
print(f"Sua idade é de {anos} anos, {meses} meses e {dias} dias.")
