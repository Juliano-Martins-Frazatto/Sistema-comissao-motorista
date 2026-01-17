print("================================================================")
print("Você iniciou a ferramenta de cálculo de fretes!")
print(f"----------------------------------------------------------------\n")


def converter_entrada_de_dados(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: digite apenas números")


while True:
    valor_frete_ida = converter_entrada_de_dados(
        "Valor do frete de ida (verificar se o vale pedágio não está incluso, se estiver, subtraia o valor do mesmo!):")

    valor_frete_volta = converter_entrada_de_dados(
        "Valor do frete de volta (verificar se o vale pedágio não está incluso, se estiver, subtraia o valor do mesmo!):")

    soma_frete_ida_e_volta = valor_frete_ida + valor_frete_volta

    print(f"Valor do frete ida + frete volta: {soma_frete_ida_e_volta}")

    pedagio_ida_dinheiro = converter_entrada_de_dados(
        "Pedagio de ida no dinheiro:")

    pedagio_volta_dinheiro = converter_entrada_de_dados(
        "Pedágio de volta no dinheiro:")

    soma_ped_ida_e_volta_dinheiro = pedagio_ida_dinheiro + pedagio_volta_dinheiro

    print(
        f"Soma dos pedágios de ida e volta no dinheiro:{soma_ped_ida_e_volta_dinheiro}")

    vale_viagem = converter_entrada_de_dados("Vale para viagem:")

    outras_despesas_dinheiro = converter_entrada_de_dados(
        "Outras despesas no dinheiro(será descontado do vale):")

    conta_comissao = (
        (soma_frete_ida_e_volta - soma_ped_ida_e_volta_dinheiro) * 12)/100
    print(f"Comissão bruta:{conta_comissao}")

    conta_vale = vale_viagem - outras_despesas_dinheiro
    if conta_vale < 0:
        print("===Vale insuficiente===")
        conta_vale_insuficiente = conta_vale * -1
        print("O valor excedido do vale será pago junto com a comissão!")
        conta_comissao_final_vale_insuficiente = conta_comissao + conta_vale_insuficiente
        print(
            f"Pagar para o motorista: {conta_comissao_final_vale_insuficiente}")

    else:
        print(
            f"Sobrou {conta_vale} de vale. O valor será descontado da comissão")
        conta_vale_suficiente = conta_comissao - conta_vale
        print(f"Pagar para o motorista:{conta_vale_suficiente}")
