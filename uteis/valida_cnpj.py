def valida_cnpj(cnpj):
    cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")
    if len(cnpj) != 14:
        return False

    soma = 0
    pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(12):
        soma += int(cnpj[i]) * pesos[i]
    resto = soma % 11
    if resto < 2:
        dv1 = 0
    else:
        dv1 = 11 - resto
    if int(cnpj[12]) != dv1:
        return False

    soma = 0
    pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(13):
        soma += int(cnpj[i]) * pesos[i]
    resto = soma % 11
    if resto < 2:
        dv2 = 0
    else:
        dv2 = 11 - resto
    if int(cnpj[13]) != dv2:
        return False

    return True

