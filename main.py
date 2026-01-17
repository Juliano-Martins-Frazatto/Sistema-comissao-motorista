
reset = "\033[0m"
verde = "\033[92m"
vermelho = "\033[91m"


def converter_entrada_de_dados(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: digite apenas números")


print(
    f"{verde}================================================================\n")
print("Você iniciou a ferramenta de cálculo de fretes!\n")
print(
    f"----------------------------------------------------------------\n{reset}")

while True:
    valor_frete_ida = converter_entrada_de_dados(
        f"\nValor do frete de ida (verificar se o vale pedágio não está incluso, se estiver, subtraia o valor do mesmo!):")

    valor_frete_volta = converter_entrada_de_dados(
        f"\nValor do frete de volta (verificar se o vale pedágio não está incluso, se estiver, subtraia o valor do mesmo!):")

    soma_frete_ida_e_volta = valor_frete_ida + valor_frete_volta

    print(
        f"{verde}\n============================================================")
    print(f"\nValor do frete ida + frete volta: {soma_frete_ida_e_volta}")
    print(
        f"\n============================================================{reset}")

    pedagio_ida_dinheiro = converter_entrada_de_dados(
        f"\nPedágio de ida no dinheiro:")

    pedagio_ida_tag = converter_entrada_de_dados(f"\nPedágio de ida na TAG:")

    pedagio_volta_dinheiro = converter_entrada_de_dados(
        f"\nPedágio de volta no dinheiro:")

    pedagio_volta_tag = converter_entrada_de_dados(
        f"\nPedágio de volta na TAG:")

    soma_ped_ida_e_volta_dinheiro = pedagio_ida_dinheiro + pedagio_volta_dinheiro

    soma_ped_ida_e_volta_tag = pedagio_ida_tag + pedagio_volta_tag

    print(
        f"{verde}\n============================================================")
    print(
        f"\nSoma dos pedágios de ida e volta no dinheiro:{soma_ped_ida_e_volta_dinheiro}")

    print(
        f"\nSoma dos pedágios de ida e volta na TAG:{soma_ped_ida_e_volta_tag}{reset}")

    vale_viagem = converter_entrada_de_dados(f"\nVale para viagem:")

    outras_despesas_dinheiro = converter_entrada_de_dados(
        f"\nOutras despesas no dinheiro(será descontado do vale):")

    conta_comissao = (
        ((soma_frete_ida_e_volta - (soma_ped_ida_e_volta_tag + soma_ped_ida_e_volta_dinheiro)) * 12)/100)
    print(
        f"{verde}\n============================================================")
    print(f"\nComissão bruta:{conta_comissao}")
    print(
        f"\n============================================================{reset}")

    conta_vale = vale_viagem - outras_despesas_dinheiro

    if conta_vale < 0:
        print("===Vale insuficiente===")

        conta_vale_insuficiente = conta_vale * -1

        print("O valor excedido do vale será pago junto com a comissão!")

        conta_comissao_final_vale_insuficiente = conta_comissao + conta_vale_insuficiente

        print(
            f"\nPagar para o motorista: {conta_comissao_final_vale_insuficiente}")

    else:
        print(
            f"\nSobrou {conta_vale} de vale. O valor será descontado da comissão")

        conta_vale_suficiente = conta_comissao - conta_vale

        print(f"\nPagar para o motorista:{conta_vale_suficiente}")
