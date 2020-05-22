# Calculo do IRPF
bruto = float(input("Salario bruto: "))
if bruto <= 1903.98:
    irpf = 0
else:
    if bruto <= 2826.65:
        irpf = bruto * 7.5/100 - 142.80
    else:
        if bruto <= 3751.05:
            irpf = bruto * 15/100 - 354.80
        else:
            if bruto <= 4664.68:
                irpf = bruto * 22.5/100 - 636.13
            else:
                irpf = bruto * 27.5/100 - 869.36

# Isso trata erros de arrendondamento
if irpf < 0:
    irpf = 0

liquido = bruto - irpf
print ("Salario Bruto ", bruto)
print ("IRPF ", irpf)
print ("Salario Líquido ", liquido)









