def leia_int(msg):
    while True:
        try:
            mensagem = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO, Digite um número inteiro válido\033[m')
            continue
        else:
            return mensagem

def leia_float(msg):
    while True:
        try:
            mensagem = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO, digite um número decimal válido\033[m')
            continue
        else:
            return mensagem