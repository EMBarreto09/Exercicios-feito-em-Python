def leia_dinheiro(msg):
    while True:
        mensagem = str(input(msg)).strip().replace(',','.')

        if mensagem.isalpha() or mensagem == "":
            print(f'ERRO, \"{mensagem}\" está inválida')
        else:
            return float(mensagem)
          