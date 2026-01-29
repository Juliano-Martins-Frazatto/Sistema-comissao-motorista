reset = "\033[0m"
verde = "\033[92m"

Historico = {}


def guardar_historico_txt():
    arquivo = open("historico.txt", "a", encoding="utf-8")
    for chave, valor in Historico.items():
        arquivo.write(f"{chave}:{valor}\n")
    arquivo.write("====================================================")
    arquivo.close()


def cor_verde(mensagem):
    print(f"{verde}{mensagem}{reset}")


def continuar_sn():
    while True:

        continuar = input("Deseja continuar?[s/n]:").lower().strip()

        if continuar == "n":
            print("Você saiu do programa")

            return False

        elif continuar == "s":

            print("Continuando -------------------->")

            break

        else:
            print("Digite apenas opções válidas [s/n]")


def converter_entrada_de_dados_numeros(mensagem):
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


def conta_vale():

    conta_do_vale = vale_viagem - outras_despesas_dinheiro

    if conta_do_vale < 0:

        conta_vale_condicao = conta_do_vale * -1

        conta_comissao_final_vale_insuficiente = comissao_bruta + conta_vale_condicao
        cor_verde(
            f"vale insuficiente===\n                                                     O valor excedido do vale será pago junto com a comissão!\n==================================================================\nPagar para o motorista: {conta_comissao_final_vale_insuficiente}\n===============================================================          ")
        return conta_comissao_final_vale_insuficiente
    else:
        conta_vale_condicao = comissao_bruta - conta_do_vale

        cor_verde(
            f"\n===========================================================    \nSobrou {conta_do_vale} de vale. Esse valor será descontado da comissão.\nPagar para o motorista:{conta_vale_condicao}\n===========================================================            ")
    return conta_vale_condicao


cor_verde("============================================================\n       \nBem-vindo\n                        \n============================================================\n")


while True:

    nome_motorista = input("Digite o nome do motorista: ")

    placa_cavalo = input("\nDigite a placa do cavalo:").upper()

    placa_carreta = input("\nDigite a placa da carreta: ").upper()

    valor_frete_ida = converter_entrada_de_dados_numeros(
        f"\nValor do frete de ida (verificar se o vale pedágio não está incluso, se estiver, subtraia o valor do mesmo!):")

    valor_frete_volta = converter_entrada_de_dados_numeros(
        f"\nValor do frete de volta (verificar se o vale pedágio não está incluso, se estiver, subtraia o valor do mesmo!):")

    cor_verde(
        f"============================================================\n           Valor do frete ida + frete volta: {calculo_frete(valor_frete_ida, valor_frete_volta)}    \n============================================================")

    pedagio_ida_dinheiro = converter_entrada_de_dados_numeros(
        f"\nPedágio de ida no dinheiro:")

    pedagio_ida_tag = converter_entrada_de_dados_numeros(
        f"\nPedágio de ida na TAG:")

    pedagio_volta_dinheiro = converter_entrada_de_dados_numeros(
        f"\nPedágio de volta no dinheiro:")

    pedagio_volta_tag = converter_entrada_de_dados_numeros(
        f"\nPedágio de volta na TAG:")

    cor_verde(f"{verde}\n============================================================       \nSoma dos pedágios de ida e volta no dinheiro:{soma_ped_dinheiro(pedagio_ida_dinheiro, pedagio_volta_dinheiro)}                    \nSoma dos pedágios de ida e volta na TAG:{soma_ped_tag(pedagio_ida_tag, pedagio_volta_tag)}\n============================================================{reset}")

    vale_viagem = converter_entrada_de_dados_numeros(f"\nVale para viagem:")

    outras_despesas_dinheiro = converter_entrada_de_dados_numeros(
        f"\nOutras despesas no dinheiro(será descontado do vale):")

    comissao_bruta = calculo_comissao_bruta(
        valor_frete_ida,
        valor_frete_volta,
        pedagio_ida_tag,
        pedagio_volta_tag,
        pedagio_ida_dinheiro,
        pedagio_volta_dinheiro
    )

    conta_vale()

    cor_verde(
        f"{verde}\n============================================================\nComissão bruta:{comissao_bruta}\n============================================================{reset}")

    conta_do_vale = vale_viagem - outras_despesas_dinheiro

    # Adiciona a mensagem de entrada e o dado recebido no Histórico
    Historico["Motorista"] = nome_motorista
    Historico["Placa do cavalo"] = placa_cavalo
    Historico["Placa do carreta"] = placa_carreta
    Historico["Frete ida"] = valor_frete_ida
    Historico['Frete volta'] = valor_frete_volta
    Historico["Pedágio de ida no dinheiro"] = pedagio_ida_dinheiro
    Historico["Pedágio de ida na TAG"] = pedagio_ida_tag
    Historico["Pedágio de volta no dinheiro"] = pedagio_volta_dinheiro
    Historico["Pedágio de volta na TAG"] = pedagio_volta_tag
    Historico["vale para viagem"] = vale_viagem
    Historico["Outras despesas (no dinheiro)"] = outras_despesas_dinheiro
    Historico["Comissão"] = comissao_bruta
    Historico["Sobra do vale"] = conta_do_vale
    Historico["Pagar para o motorista"] = conta_vale()

    guardar_historico_txt()

    continuar_sn()
