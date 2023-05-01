def valida_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")  
    if len(cpf) != 11 or not cpf.isdigit(): 
        return False

    soma = 0
    for i, mult in zip(range(10, 1, -1), cpf[:9]):
        soma += i * int(mult)
    digito1 = 11 - soma % 11 if soma % 11 > 1 else 0
    if digito1 != int(cpf[9]):
        return False

    soma = 0
    for i, mult in zip(range(11, 1, -1), cpf[:10]):
        soma += i * int(mult)
    digito2 = 11 - soma % 11 if soma % 11 > 1 else 0
    if digito2 != int(cpf[10]):
        return False

    return True 