reset = "\033[0m"
verde = "\033[92m"


def cor_verde(mensagem):
    print(f"{verde}{mensagem}{reset}")


def converter_entrada_de_dados(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: digite apenas números")


def calculo_frete(valor_frete_ida, valor_frete_volta):
    resultado = valor_frete_ida + valor_frete_volta
    return resultado


def soma_ped_dinheiro(pedagio_ida_dinheiro, pedagio_volta_dinheiro):
    resultado = pedagio_ida_dinheiro + pedagio_volta_dinheiro
    return resultado


def soma_ped_tag(pedagio_ida_tag, pedagio_volta_tag):
    resultado = pedagio_ida_tag + pedagio_volta_tag
    return resultado


def calculo_comissao_bruta(
    valor_frete_ida,
    valor_frete_volta,
    pedagio_ida_tag,
    pedagio_volta_tag,
    pedagio_ida_dinheiro,
    pedagio_volta_dinheiro
):
    soma_frete = calculo_frete(valor_frete_ida, valor_frete_volta)
    soma_despesas = soma_ped_tag(pedagio_ida_tag, pedagio_volta_tag) + \
        soma_ped_dinheiro(pedagio_ida_dinheiro, pedagio_volta_dinheiro)

    porcentagem = (soma_frete - soma_despesas) * 12

    conta_comissao = porcentagem / 100
    return conta_comissao


cor_verde("============================================================\n       \nBem-vindo\n                        \n============================================================")

while True:
    valor_frete_ida = converter_entrada_de_dados(
        f"\nValor do frete de ida (verificar se o vale pedágio não está incluso, se estiver, subtraia o valor do mesmo!):")

    valor_frete_volta = converter_entrada_de_dados(
        f"\nValor do frete de volta (verificar se o vale pedágio não está incluso, se estiver, subtraia o valor do mesmo!):")

    cor_verde(
        f"============================================================\n           Valor do frete ida + frete volta: {calculo_frete(valor_frete_ida, valor_frete_volta)}    \n============================================================")

    pedagio_ida_dinheiro = converter_entrada_de_dados(
        f"\nPedágio de ida no dinheiro:")

    pedagio_ida_tag = converter_entrada_de_dados(f"\nPedágio de ida na TAG:")

    pedagio_volta_dinheiro = converter_entrada_de_dados(
        f"\nPedágio de volta no dinheiro:")

    pedagio_volta_tag = converter_entrada_de_dados(
        f"\nPedágio de volta na TAG:")

    cor_verde(f"{verde}\n============================================================       \nSoma dos pedágios de ida e volta no dinheiro:{soma_ped_dinheiro(pedagio_ida_dinheiro, pedagio_volta_dinheiro)}                    \nSoma dos pedágios de ida e volta na TAG:{soma_ped_tag(pedagio_ida_tag, pedagio_volta_tag)}\n============================================================{reset}")

    vale_viagem = converter_entrada_de_dados(f"\nVale para viagem:")

    outras_despesas_dinheiro = converter_entrada_de_dados(
        f"\nOutras despesas no dinheiro(será descontado do vale):")

    comissao_bruta = calculo_comissao_bruta(
        valor_frete_ida,
        valor_frete_volta,
        pedagio_ida_tag,
        pedagio_volta_tag,
        pedagio_ida_dinheiro,
        pedagio_volta_dinheiro
    )
    cor_verde(
        f"{verde}\n============================================================\nComissão bruta:{comissao_bruta}\n============================================================{reset}")

    conta_vale = vale_viagem - outras_despesas_dinheiro

    if conta_vale < 0:

        conta_vale_insuficiente = conta_vale * -1

        conta_comissao_final_vale_insuficiente = comissao_bruta + conta_vale_insuficiente
        cor_verde(
            f"vale insuficiente===\n                                                     O valor excedido do vale será pago junto com a comissão!\n==================================================================\nPagar para o motorista: {conta_comissao_final_vale_insuficiente}\n===============================================================          ")

    else:
        conta_vale_suficiente = comissao_bruta - conta_vale

        cor_verde(
            f"\n===========================================================    \nSobrou {conta_vale} de vale. Esse valor será descontado da comissão.\nPagar para o motorista:{conta_vale_suficiente}\n===========================================================            ")
